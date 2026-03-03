# simple_python_website.py

from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # Yo HTML content directly Python string maa
        html_content = """
        <html>
        <head><title>Aalu AI</title></head>
        <body style='text-align:center; margin-top:100px; font-family:Arial;'>
            <h1>Hello, I am Aalu</h1>
            <p>Yo website sirf Python le banako ho.</p>
        </body>
        </html>
        """
        self.wfile.write(html_content.encode('utf-8'))

# server run
port = 8080
server = HTTPServer(('localhost', port), SimpleHandler)
print(f"Server running at http://localhost:{port}")
server.serve_forever()