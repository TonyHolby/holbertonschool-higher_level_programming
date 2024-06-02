import http.server
import socketserver
import json

""" Defines a subclass to set up a simple HTTP server. """


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """ Defines a do_GET method that handles GET requests.

        Args:
            http.server.BaseHTTPRequestHandler : A class from the http.server
            module that handles HTTP requests.
    """
    def do_GET(self):
        """ Sends a simple text or a JSON response back to the client. """
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info_version = {"version": "1.0", "description": """A \
                            simple API built with http.server"""}
            self.wfile.write(json.dumps(info_version).encode("utf-8"))
        else:
            self.send_error(404, "Endpoint not found")


PORT = 8000
with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
