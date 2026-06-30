const { app, BrowserWindow } = require('electron');
const path = require('path');

function createWindow() {
    const mainWindow = new BrowserWindow({
        width: 1300,
        height: 800,
        webPreferences: {
            // WARNING: Disabling webSecurity should ONLY be done for trusted internal content like this dashboard, 
            // especially when testing external APIs that don't support CORS.
            webSecurity: false, 
            preload: path.join(__dirname, 'preload.js'),
            nodeIntegration: true, // Enable nodeIntegration for local file access
            contextIsolation: false // Disable contextIsolation for simpler setup
        }
    });

    mainWindow.loadFile('aurora_integrated_dashboard.html');

    // Open the DevTools.
    mainWindow.webContents.openDevTools();

    // CORS BYPASS FIX: This explicitly overrides the response headers to allow all origins,
    // which is often necessary when webSecurity: false isn't enough for external APIs.
    mainWindow.webContents.session.webRequest.onHeadersReceived((details, callback) => {
        callback({
            responseHeaders: {
                ...details.responseHeaders,
                'Content-Security-Policy': [''],
                'Access-Control-Allow-Origin': ['*'],
                'Access-Control-Allow-Headers': ['*']
            }
        });
    });
}

app.whenReady().then(() => {
    createWindow();

    app.on('activate', function () {
        if (BrowserWindow.getAllWindows().length === 0) createWindow();
    });
});

app.on('window-all-closed', function () {
    if (process.platform !== 'darwin') app.quit();
});
