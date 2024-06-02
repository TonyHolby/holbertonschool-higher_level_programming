from http.server import HTTPServer, BaseHTTPRequestHandler
import json

""" Defines a subclass to set up a simple HTTP server. """


class Subclass(BaseHTTPRequestHandler):
    """ Defines a do_GET method that handles GET requests.

        Args:
            BaseHTTPRequestHandler : A class from the http.server
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
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b'{"version": "1.0", "description": "A simple API built with http.server"}')
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found")


httpd = HTTPServer(("", 8000), Subclass)
httpd.serve_forever()
