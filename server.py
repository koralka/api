from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from datetime import datetime



class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"message": "Hello, World!"}).encode())
        elif self.path == "/time":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            current_time = datetime.now().isoformat()
            self.wfile.write(json.dumps({"time": current_time}).encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Not Found"}).encode())    
                
localhost = "localhost"
port = 8000

server = HTTPServer((localhost, port), MyHandler)

if __name__ == "__main__":
    print(f"Server started http://{localhost}:{port}")
    server.serve_forever()
    



    
