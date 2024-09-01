#!/usr/bin/env python3
import socket
import sys

porta = int(input('Entre com a porta do servidor'))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.bind(('', porta))
except:
   print('# erro de bind')
   sys.exit()

while True:
    data, addr = s.recvfrom(1024)
    print('sensor ', addr, ' enviou:', data)

print('o servidor encerrou')
s.close()