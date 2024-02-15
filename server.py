import http.server
import json
from urllib.parse import urlparse, parse_qs
PORT = 3000

class JSONHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        parsed_url = urlparse(self.path)
        path_components = parsed_url.path.split('/')
        
        if len(path_components) >2:
            slug = path_components[2]
        else:
            slug=""
        try:
            with open('response.json', 'r') as file:
                data = json.loads(file.read())
                # print(data)
                # print(data["result"])
                for i in data["result"]:
                    if i["name"].lower()==slug.lower():

                        self.wfile.write(json.dumps(i).encode())
            
        except FileNotFoundError:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(b'Error reading JSON file')
server_address = ('', PORT)
httpd = http.server.HTTPServer(server_address, JSONHandler)
print(f"Server running on port {PORT}")
httpd.serve_forever()

# import requests
# name = ""
# company = requests.get(f"localhost:3000/companies/?name={name}")