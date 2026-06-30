const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
    loginWithGoogle: () => ipcRenderer.invoke('google-oauth-login'),
    loginWithQuantal: () => ipcRenderer.invoke('quantal-oauth-login'),
    getAuthStatus: () => ipcRenderer.invoke('get-auth-status'),
    getAccessToken: () => ipcRenderer.invoke('get-access-token'),
    chatGemini: (prompt) => ipcRenderer.invoke('gemini:chat', prompt),
    logout: () => ipcRenderer.invoke('google-oauth-logout'),
    onAuthUpdate: (callback) => ipcRenderer.on('auth-update', (event, status) => callback(status))
});

window.addEventListener('DOMContentLoaded', () => {
    const replaceText = (selector, text) => {
        const element = document.getElementById(selector);
        if (element) element.innerText = text;
    };

    for (const type of ['chrome', 'node', 'electron']) {
        replaceText(`${type}-version`, process.versions[type]);
    }
});