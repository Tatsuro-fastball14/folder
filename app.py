from http.server import simpleHTTPRequestHandler, HTTPServer

server = HTTPServer(('',8000), simpleHTTPRequestHandler ) 
server.serve_forever()