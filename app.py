import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = {
            "status": "running",
            "service": "myapp",
        }
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

server = HTTPServer(("0.0.0.0", 5000), Handler)
server.serve_forever()
