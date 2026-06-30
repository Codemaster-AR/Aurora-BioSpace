const crypto = require('crypto');

function base64UrlEncode(buffer) {
    return buffer.toString('base64')
        .replace(/\+/g, '-')
        .replace(/\//g, '_')
        .replace(/=/g, '');
}

function generateVerifier() {
    return base64UrlEncode(crypto.randomBytes(32));
}

function generateChallenge(verifier) {
    const hash = crypto.createHash('sha256').update(verifier).digest();
    return base64UrlEncode(hash);
}

module.exports = {
    generateVerifier,
    generateChallenge
};
