#!/usr/bin/env python
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import struct

# Some observations:
# 1. The pairing server MUST set the Content-Length in the HTTP response.
# 2. The 'cmnm' value returned by the pairing server MUST match the
#    DvNm (device name) advertised in the DNS-SD service
class PairingHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    # any incoming requests are just pairing code related
    # return our guid regardless of input

    values = {
      'cmpg': '\x00\x00\x00\x00\x00\x00\x00\x01',
      'cmnm': 'fezmonkey_test',
      'cmty': 'iPod',
      }

    encoded = ''
    for key, value in values.iteritems():
      encoded += '%s%s%s' % (key, struct.pack('>i', len(value)), value)
    header = 'cmpa%s' % (struct.pack('>i', len(encoded)))
    encoded = '%s%s' % (header, encoded)

    self.send_response(200)
    self.send_header('Content-Length', len(encoded))
    self.end_headers()
    self.wfile.write(encoded)

    return

try:
  port = 50006
  server = HTTPServer(('', port), PairingHandler)
  print 'started server on port %s' % (port)
  server.serve_forever()

except KeyboardInterrupt:
  server.socket.close()
