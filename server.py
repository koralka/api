from http.server import BaseHTTPRequestHandler, HTTPServer
import json



class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        dict_data = {"key": "value"}
        json_dump = json.dumps(dict_data)
        print(json_dump)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json_dump.encode())
        
        
localhost = "localhost"
port = 8000

server = HTTPServer((localhost, port), MyHandler)

if __name__ == "__main__":
    print(f"Server started http://{localhost}:{port}")
    server.serve_forever()
    



    
