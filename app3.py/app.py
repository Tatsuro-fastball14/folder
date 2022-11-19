from http.server import BaseHTTPRequestHandler, HTTPServer
class HelloServerHandler(BaseHTTPRequestHandler):
 def do_get(self):
  self.send_response(200)
  self.end_headers()
  self/wfile.write(b'sampleweb-server!!!')

server = HTTPServer(('',8000), HelloServerHandle ) 
server.serve_forever()