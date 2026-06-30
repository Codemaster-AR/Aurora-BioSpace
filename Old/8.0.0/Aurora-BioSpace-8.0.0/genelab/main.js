const { app, BrowserWindow, ipcMain, shell, session } = require('electron');
const path = require('path');
const { spawn } = require('child_process');
const { OAuth2Client } = require('google-auth-library');
const fs = require('fs');
const http = require('http');
const { generateVerifier, generateChallenge } = require('./utils/auth');

let mainWindow;
let proxyProcess;
let oAuth2Client = {
    credentials: {}
};
let isAuthenticated = false;
let authProvider = null; 

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1400, height: 900,
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: true,
      nodeIntegration: false,
      sandbox: true,
      webviewTag: true
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
                oAuth2Client.credentials = data.tokens || {};
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
  
  function startProxy() {
      proxyProcess = spawn('node', [proxyPath], { cwd: __dirname, detached: false });
      
      proxyProcess.on('error', (err) => {
        console.error(`DEBUG: Failed to start proxy process: ${err.message}`);
      });

      proxyProcess.on('close', (code) => {
        console.log(`DEBUG: Proxy process exited with code ${code}. Restarting in 5s...`);
        setTimeout(startProxy, 5000); // Add a delay to prevent rapid crash-loops
      });
      
      proxyProcess.stdout.on('data', (data) => console.log(`Proxy: ${data}`));
      proxyProcess.stderr.on('data', (data) => console.error(`Proxy Error: ${data}`));
  }
  
  startProxy();
  
  loadSession();
  setupHandlers();
  createWindow();
});

async function startOAuthFlow() {
  const verifier = generateVerifier();
  const challenge = generateChallenge(verifier);
  const clientId = '1073478097806-e1uppnsvsmddbqp1hifdt2s8iqjrp7ns.apps.googleusercontent.com';
  const redirectUri = 'http://localhost:3000';
  const scope = 'openid email profile https://www.googleapis.com/auth/generative-language.tuning';
  
  const authUrl = `https://accounts.google.com/o/oauth2/v2/auth?` +
    `client_id=${clientId}&` +
    `redirect_uri=${encodeURIComponent(redirectUri)}&` +
    `response_type=code&` +
    `scope=${encodeURIComponent(scope)}&` +
    `code_challenge=${challenge}&` +
    `code_challenge_method=S256`;

  return new Promise((resolve, reject) => {
    let authWindow = new BrowserWindow({ 
        width: 600, 
        height: 800, 
        webPreferences: { 
            nodeIntegration: false, 
            contextIsolation: true 
        }
    });

    let codeProcessed = false;
    authWindow.webContents.on('did-fail-load', (event, errorCode, errorDescription) => {
        console.error(`DEBUG: Auth window failed to load: ${errorDescription} (${errorCode})`);
    });

    const server = http.createServer(async (req, res) => {
        const url = new URL(req.url, `http://${req.headers.host}`);
        const code = url.searchParams.get('code');
        console.log("DEBUG: HTTP Server received request:", req.url);
        
        if (code && !codeProcessed) {
            codeProcessed = true;
            console.log("DEBUG: Auth code received in HTTP server:", code);
            res.end('Authentication successful. You can close this window.');
            server.close();
            console.log("DEBUG: HTTP server closed");
            
            // Try closing the window safely
            if (authWindow && !authWindow.isDestroyed()) {
                console.log("DEBUG: Closing auth window");
                authWindow.close();
            }
            authWindow = null; // Important: nullify the reference
            
            
            console.log("DEBUG: Sending verifier to proxy:", verifier);
            
            // Ensure you grab the codeVerifier variable that was generated 
            // when you created the auth URL challenge!
            try {
                const response = await fetch("https://quantal-labs.com/google-auth/aurora-biospace-auth/auth", {
                  method: "POST",
                  headers: {
                    "Content-Type": "application/json"
                  },
                  body: JSON.stringify({
                    code: code,                      // The code from your log
                    redirectUri: redirectUri,
                    codeVerifier: verifier           // <-- Send the plaintext verifier here!
                  })
                });
                const rawResponse = await response.text();
                console.log("DEBUG: Raw response from proxy:", rawResponse);
                
                let tokens;
                try {
                    tokens = JSON.parse(rawResponse);
                } catch (e) {
                    console.error("DEBUG: Failed to parse proxy response", e);
                    throw new Error("Failed to parse proxy response as JSON");
                }
                
                console.log("DEBUG: Received tokens from proxy:", !!tokens.access_token);
                
                if (!tokens.access_token) {
                    console.error("DEBUG: No access_token in proxy response");
                    throw new Error("No access_token in proxy response");
                }
                
                oAuth2Client.credentials = tokens;
                isAuthenticated = true;
                authProvider = 'google';
                saveSession({ provider: 'google', tokens: oAuth2Client.credentials });
                
                // Notify renderer that auth is complete
                if (mainWindow) {
                    mainWindow.webContents.send('auth-update', { isLoggedIn: true, provider: 'google' });
                }
                
                console.log("DEBUG: Auth success, resolving promise");
                resolve({ isLoggedIn: true, user: { name: 'User' } });
            } catch (err) {
                console.error("DEBUG: Token exchange failed:", err);
                isAuthenticated = false;
                authProvider = null;
                reject(err);
            }
        } else if (codeProcessed) {
            console.log("DEBUG: Code already processed, ignoring request");
            res.end('Authentication already processed.');
        } else {
            console.log("DEBUG: No code found in callback, URL:", req.url);
            res.end('No code found.');
        }
    });

    server.listen(3000, () => {
        authWindow.loadURL(authUrl);
    });

    authWindow.on('closed', () => {
        if(server.listening) server.close();
        if (!isAuthenticated) resolve({ isLoggedIn: false });
    });
  });
}

function setupHandlers() {
  ipcMain.handle('get-auth-status', () => ({ isLoggedIn: isAuthenticated, provider: authProvider }));
  ipcMain.handle('google-oauth-login', async () => {
      return await startOAuthFlow();
  });
// ... rest of setupHandlers unchanged
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
    oAuth2Client.credentials = {}; // Clear credentials
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
            const accessToken = oAuth2Client.credentials.access_token;
            if (!accessToken) {
                throw new Error("No access token available.");
            }
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
