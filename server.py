from http.server import HTTPServer, CGIHTTPRequestHandler
server_data = ("localhost", 5555)
server = HTTPServer(server_data, CGIHTTPRequestHandler)

print("Server is Connected...")
server.serve_forever()  

