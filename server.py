from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import webbrowser

PORT_NUMBER = 2144

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write("URL-Poke is running on your machine. Uh oh.")
        return

    def do_POST(self):
        length = int(self.headers.getheader('content-length'))
        link = self.headers.getheader('link')
        postvars = self.rfile.read(length)
        print link
        webbrowser.open_new(link)

        resp = "Opened " + link + " on target. Ha."

        self.send_response(200)
        self.send_header('msg', resp)
        self.end_headers()

try:
    server = HTTPServer(('', PORT_NUMBER), Server)
    print 'Started URL-Poke server on port ' , PORT_NUMBER
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the web server'
    server.socket.close()