#!/usr/bin/env python3
import socket
import sys
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setblocking(0)

while True:
    ip = input('Entre com o IP de destino: ')
    porta = int(input('Entre com a porta de destino: '))
    msg = input('Entre com a mensagem: ')
    data = bytes(msg, 'utf-8') 
    s.sendto(data, (ip, porta))
    time.sleep(5)
    try:
        data, addr = s.recvfrom(1024)
        print(f'Servidor me enviou:{data}')
    except:
        print(f'Servidor nao recebeu!')


print('o cliente encerrou')
s.close()