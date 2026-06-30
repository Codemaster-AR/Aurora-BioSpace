const fs = require('fs');
const util = require('util');
const logFile = fs.createWriteStream('proxy.log', { flags: 'a' });
// Redirect console.log and console.error to the log file
console.log = function () {
    logFile.write(util.format.apply(null, arguments) + '\n');
    process.stdout.write(util.format.apply(null, arguments) + '\n');
};
console.error = function () {
    logFile.write(util.format.apply(null, arguments) + '\n');
    process.stderr.write(util.format.apply(null, arguments) + '\n');
};

// Global error handlers
process.on('uncaughtException', (err) => {
    console.error('UNCAUGHT EXCEPTION:', err);
    process.exit(1);
});
process.on('unhandledRejection', (reason, promise) => {
    console.error('UNHANDLED REJECTION:', reason);
    process.exit(1);
});

const express = require('express');
const cors = require('cors');
const myFetch = require('node-fetch');

const app = express();
const PORT = 3001; // Choose a port for your proxy server

// Allow CORS for the Electron renderer process
app.use(cors());
app.use(express.json()); // To parse JSON request bodies

// Define the GeneLab API base URL
const GENELAB_API_BASE = 'https://osdr.nasa.gov/osdr/data/search';

// Proxy endpoint
app.get('/proxy-genelab', async (req, res) => {
    const searchTerm = req.query.term || ''; // Get the search term from the frontend
    const apiUrlWithParams = `${GENELAB_API_BASE}?term=${encodeURIComponent(searchTerm)}&size=100`;
    console.log(`Proxy calling NASA API: ${apiUrlWithParams}`);

    try {
        // Forward the request to the actual GeneLab API
        const response = await myFetch(apiUrlWithParams, {
            headers: { 'User-Agent': 'AuroraBioscienceDashboard/1.0' }
        });
        if (!response.ok) {
            console.error(`NASA API responded with status: ${response.status}`);
            const errorText = await response.text();
            console.error(`NASA API error response: ${errorText}`);
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        res.json(data);
    } catch (error) {
        console.error('Proxy error:', error);
        // Ensure we send a response even on error
        if (!res.headersSent) {
            res.status(500).json({ error: 'Failed to fetch data from GeneLab API' });
        }
    }
});

app.listen(PORT, (err) => {
    if (err) {
        console.error('Failed to listen on port', PORT, err);
        process.exit(1);
    }
    console.log(`Proxy server listening on port ${PORT}`);
});
