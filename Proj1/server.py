#!/usr/bin/env python3

# Example HTTP server
#
# See <https://docs.python.org/3/library/http.server.html> for details


import http.server
import socketserver
import json
import sys
import urllib


PORT = 8080


class ExampleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()

        headers = {'Accept': 'application/json'}
        conn = http.client.HTTPSConnection("www.foaas.com")
        conn.request('GET', path, headers=headers)
        r1 = conn.getresponse()
        print(r1.status, r1.reason)
        data1 = r1.read()
        print(data1)
        dictionary = json.loads(data1)
        #makes the message safe to pass into purgomalum
        safeString = urllib.parse.quote(dictionary['message'], safe='/', encoding=None, errors=None)
        print(safeString)

        conn2 = http.client.HTTPSConnection("www.purgomalum.com")
        conn2.request('GET', "/service/json?text="+safeString)
        r2 = conn2.getresponse()
        print(r2.status, r2.reason)
        data2 = r2.read()  
        dictionary2 = json.loads(data2)
        dictionary2['subtitle'] = dictionary['subtitle']
        payload = (
            f'<!DOCTYPE html> <html> <head> <title>FOAAS - {dictionary2["result"]} {dictionary2["subtitle"]}</title> <meta charset="utf-8"> <meta property="og:title" content="{dictionary2["result"]} {dictionary2["subtitle"]}"> <meta property="og:description" content="{dictionary2["result"]} {dictionary2["subtitle"]}"> <meta name="twitter:card" content="summary" /> <meta name="twitter:site" content="@foaas" /> <meta name="twitter:title" content="FOAAS: Fuck Off As A Service" /> <meta name="twitter:description" content="{dictionary2["result"]} {dictionary2["subtitle"]}" /> <meta name="viewport" content="width=device-width, initial-scale=1"> <link href="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.2/css/bootstrap-combined.min.css" rel="stylesheet"> </head> <body style="margin-top:40px;"> <div class="container"> <div id="view-10"> <div class="hero-unit"> <h1>{dictionary2["result"]}</h1> <p><em>{dictionary2["subtitle"]}</em></p> </div> </div> <p style="text-align: center"><a href="http://foaas.com">foaas.com</a></p> </div> </body> </html>'
        )
        self.wfile.write(payload.encode('utf-8'))


with socketserver.TCPServer(("", PORT), ExampleHTTPRequestHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
    