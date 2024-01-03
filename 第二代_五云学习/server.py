from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from _thread import start_new_thread
from myBasics import base64ToBin, binToBase64  # pip install myBasics
from typing import Any
import json
from time import sleep

port = int(input('Port: '))

f = open('cache.json')
cache = f.read()
f.close()
cache = json.loads(cache)


class Resquest(BaseHTTPRequestHandler):
    def do_GET(self):
        url = self.path
        if (url in cache):
            print(url)
            status = cache[url][0]
            content = cache[url][1]
            self.send_response(status)
            self.end_headers()
            self.wfile.write(base64ToBin(content))
            return

    def log_message(self, format: str, *args: Any) -> None:
        pass


server = ThreadingHTTPServer(('0.0.0.0', port), Resquest)
start_new_thread(server.serve_forever, ())
print('Listening on 0.0.0.0:' + str(port) + ' ...')
print(f"Please open http://<your_ip>:{port}/docs/v9/")
while True:
    sleep(10)
