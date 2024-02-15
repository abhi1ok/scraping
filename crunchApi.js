const http = require('http');
const fs = require('fs');

// Read the JSON file
const jsonData = JSON.parse(fs.readFileSync('crunch.postman_collection.json', 'utf8'));

// Create HTTP server
const server = http.createServer((req, res) => {
    // Set the content type to JSON
    res.setHeader('Content-Type', 'application/json');

    // Handle GET requests to /api/data
    if (req.method === 'GET' && req.url === '/api/data') {
        res.writeHead(200);
        res.end(JSON.stringify(jsonData));
    } else {
        // Handle invalid routes
        res.writeHead(404);
        res.end(JSON.stringify({ error: 'Route not found' }));
    }
});

// Start the server
const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
