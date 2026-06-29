import http.server
import socketserver
import os

PORT = 5000
DIRECTORY = os.path.dirname(__file__)

class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

if __name__ == '__main__':
    handler = SimpleHTTPRequestHandler
    with socketserver.TCPServer(('', PORT), handler) as httpd:
        print(f'Servidor Python activo en http://localhost:{PORT}/')
        httpd.serve_forever()
        