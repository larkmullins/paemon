#!/usr/bin/env python

import socket
import sys

HOST = socket.gethostname()
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code: ' + str(msg[0]) + ' Message: ' + msg[1]
    sys.exit()
    
print 'Socket bound'

s.listen(5)
print 'Socket now listening'

while 1:
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    
s.close()