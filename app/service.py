from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class Handler(BaseHTTPRequestHandler):
  def do_GET(self):
    if self.path == "/users":
      body = json.dumps({"users": ["Sumit", "Ved"]}).encode()

      self.send_response(200)
      self.send_header("Content-type", "application/json")
      self.send_header("Content-Length". str(len(body)))
      self.end_headers()

      self.wfile.write(body)
    else:
      self.send_response(404)
      self.end_headers()
      self.wfile.write(b"Not Found")

server = HTTPServer(("0.0.0.0", 8001), Handler)
print("User Service running on port 8001")
server.serve_forever()
