#!/usr/bin/env python3
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    ip = input('Entre com o IP de destino: ')
    porta = int(input('Entre com a porta de destino: '))
    msg = input('Entre com a mensagem: ')
    data = bytes(msg, 'utf-8') 
    s.sendto(data, (ip, porta))

print('o cliente encerrou')
s.close()