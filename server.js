const http = require('http');
const fs = require('fs');

const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'application/json');

  // Read the JSON file
  fs.readFile('response.json', (err, data) => {
    if (err) {
      res.statusCode = 500;
      res.end('Error reading JSON file');
    } else {
      res.end(data);
    }
  });
});

server.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
