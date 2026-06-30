const { app, BrowserWindow, ipcMain, shell, session } = require('electron');
const path = require('path');
const { spawn } = require('child_process');
const { OAuth2Client } = require('google-auth-library');
const fs = require('fs');
const http = require('http');

let mainWindow;
let server;
let proxyProcess; // Added declaration
let oAuth2Client;
let isAuthenticated = false;
let authProvider = null; // 'google' or 'quantal'

const credentialsPath = path.join(__dirname, 'client_secret.json');
const credentials = JSON.parse(fs.readFileSync(credentialsPath));
const { client_id, client_secret, redirect_uris } = credentials.installed;
oAuth2Client = new OAuth2Client(client_id, client_secret, redirect_uris[0]);

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1400, height: 900,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: true,
      nodeIntegration: false,
      sandbox: true
    },
    frame: false,
    backgroundColor: '#050505'
  });
  mainWindow.loadFile('intro.html');
}

const sessionPath = path.join(__dirname, 'session.bin');

function saveSession(data) {
    fs.writeFileSync(sessionPath, JSON.stringify(data));
}

function loadSession() {
    if (fs.existsSync(sessionPath)) {
        try {
            const data = JSON.parse(fs.readFileSync(sessionPath));
            isAuthenticated = true;
            authProvider = data.provider;
            if (authProvider === 'google') {
                oAuth2Client.setCredentials(data.tokens);
            }
            return { isLoggedIn: true, provider: authProvider };
        } catch (e) {
            console.error("Failed to load session", e);
        }
    }
    return { isLoggedIn: false };
}

function clearSession() {
    if (fs.existsSync(sessionPath)) {
        fs.unlinkSync(sessionPath);
    }
}

app.whenReady().then(() => {
  const proxyPath = path.join(__dirname, 'proxy.js');
  console.log("DEBUG: Spawning proxy from:", proxyPath);
  proxyProcess = spawn('node', [proxyPath], { cwd: __dirname });
  
  proxyProcess.on('error', (err) => {
    console.error(`DEBUG: Failed to start proxy process: ${err.message}`);
  });

  proxyProcess.on('close', (code) => {
    console.log(`DEBUG: Proxy process exited with code ${code}. Restarting...`);
    proxyProcess = spawn('node', [proxyPath], { cwd: __dirname });
  });
  
  proxyProcess.stdout.on('data', (data) => console.log(`Proxy: ${data}`));
  proxyProcess.stderr.on('data', (data) => console.error(`Proxy Error: ${data}`));

  loadSession(); // Check for existing session
  setupHandlers();
  createWindow();
});

async function startAuthFlow() {
  const authUrl = oAuth2Client.generateAuthUrl({
    access_type: 'offline',
    scope: ['https://www.googleapis.com/auth/generative-language.tuning'],
    prompt: 'consent'
  });
  
  return new Promise((resolve, reject) => {
    // Basic windowed login flow
    const authWindow = new BrowserWindow({ width: 600, height: 800, webPreferences: { nodeIntegration: false, contextIsolation: true }});
    authWindow.loadURL(authUrl);
    
    // Listen for code redirect
    authWindow.webContents.on('will-redirect', async (event, url) => {
        if (url.includes('code=')) {
            const code = new URL(url).searchParams.get('code');
            const { tokens } = await oAuth2Client.getToken(code);
            oAuth2Client.setCredentials(tokens);
            isAuthenticated = true;
            authWindow.close();
            resolve({ isLoggedIn: true, user: { name: 'User' } });
        }
    });
  });
}

function setupHandlers() {
  ipcMain.handle('get-auth-status', () => ({ isLoggedIn: isAuthenticated, provider: authProvider }));
  ipcMain.handle('google-oauth-login', async () => {
      const result = await startAuthFlow();
      if(result.isLoggedIn) {
          authProvider = 'google';
          saveSession({ provider: 'google', tokens: oAuth2Client.credentials });
      }
      return result;
  });
  ipcMain.handle('quantal-oauth-login', async () => {
      // Use a modal window for Quantal Labs authentication
      return new Promise((resolve) => {
          const authWindow = new BrowserWindow({ width: 600, height: 800, webPreferences: { nodeIntegration: false, contextIsolation: true }});
          authWindow.loadURL('https://authentication.quantal-labs.com');
          
          // For now, stub the success after a short delay to mimic a successful auth
          setTimeout(() => {
              isAuthenticated = true;
              authProvider = 'quantal';
              saveSession({ provider: 'quantal' });
              authWindow.close();
              resolve({ isLoggedIn: true, user: { name: 'QuantalUser' } });
          }, 3000); // 3 seconds delay for demo purposes
      });
  });
  ipcMain.handle('google-oauth-logout', async () => {
    isAuthenticated = false;
    authProvider = null;
    clearSession();
    oAuth2Client.setCredentials({}); // Clear credentials
    return { isLoggedIn: false };
  });

  ipcMain.handle('get-access-token', async () => {
    if (!isAuthenticated || !oAuth2Client.credentials || !oAuth2Client.credentials.access_token) return null;
    return oAuth2Client.credentials.access_token;
  });

  // --- RATE LIMITER QUEUE ---
  let isProcessing = false;
  const requestQueue = [];

  async function processQueue() {
    if (isProcessing || requestQueue.length === 0) return;
    isProcessing = true;

    const { prompt, resolve, reject } = requestQueue.shift();
    const models = ['gemini-flash-latest', 'gemini-3.1-flash-lite'];
    let currentModelIndex = 0;

    async function attemptRequest(modelIndex) {
        const model = models[modelIndex];
        try {
            const accessToken = (await oAuth2Client.getAccessToken()).token;
            const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${model}:generateContent`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json', 'Authorization': `Bearer ${accessToken}` },
                body: JSON.stringify({ 
                    contents: [{ role: 'user', parts: [{ text: prompt }] }]
                })
            });
            const data = await response.json();
            
            if (data.error) {
                const isRateLimited = data.error.code === 429;
                const isHighDemand = data.error.message && data.error.message.includes('high demand');
                const isQuotaExceeded = data.error.message && data.error.message.includes('exceeded your current quota');
                
                if ((isRateLimited || isHighDemand || isQuotaExceeded) && modelIndex < models.length - 1) {
                    console.warn(`Issue on ${model} (code: ${data.error.code}, msg: ${data.error.message}), falling back to ${models[modelIndex + 1]}`);
                    return attemptRequest(modelIndex + 1);
                }
                throw new Error(data.error.message);
            }
            return { success: true, text: data.candidates?.[0]?.content?.parts?.[0]?.text };
        } catch (err) {
            throw err;
        }
    }

    try {
        const result = await attemptRequest(currentModelIndex);
        resolve(result);
    } catch (err) {
        reject(err);
    } finally {
        isProcessing = false;
        setTimeout(() => processQueue(), 2000); 
    }
  }

  ipcMain.handle('gemini:chat', async (event, prompt) => {
    if (!isAuthenticated) return { success: false, error: 'Not authenticated' };
    
    if (authProvider === 'quantal') {
        try {
            const payload = {
                model: 'openai',
                messages: [{ role: 'user', content: `${prompt} Answer directly in plain text. Do not provide code, images, search results, or HTML.` }]
            };
            const response = await fetch('https://text.pollinations.ai/', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
            let text = await response.text();
            // Aggressively strip potential HTML tags and extra whitespace
            text = text.replace(/<[^>]*>?/gm, '').trim();
            return { success: true, text: text };
        } catch (err) {
            return { success: false, error: err.message };
        }
    }

    return new Promise((resolve, reject) => {
      requestQueue.push({ prompt, resolve, reject });
      processQueue();
    });
  });
  ipcMain.on('window-control', (event, action) => {
    const window = BrowserWindow.fromWebContents(event.sender);
    if (!window) return;
    if (action === 'close') window.close();
    if (action === 'minimize') window.minimize();
    if (action === 'maximize') window.isMaximized() ? window.unmaximize() : window.maximize();
  });
}
app.on('window-all-closed', () => { if (process.platform !== 'darwin') app.quit(); });
