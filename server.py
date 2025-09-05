from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello, World!")
        
        
localhost = "localhost"
port = 8000

server = HTTPServer((localhost, port), MyHandler)

if __name__ == "__main__":
    print(f"Server started http://{localhost}:{port}")
    server.serve_forever()
    
