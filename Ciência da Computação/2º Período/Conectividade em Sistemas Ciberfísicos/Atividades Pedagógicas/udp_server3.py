#!/usr/bin/env python3
import socket
import sys

ip = input('Entre com o IP do servidor:')
porta = int(input('Entre com a porta do servidor:'))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    s.bind((ip, porta))
except:
   print('# erro de bind')
   sys.exit()

while True:
    data, addr = s.recvfrom(1024)
    print('sensor: ', addr, ' enviou:', data)
    data1 = bytes('ACK', 'utf-8') 
    s.sendto(data1, addr)

print('o servidor encerrou')
s.close()