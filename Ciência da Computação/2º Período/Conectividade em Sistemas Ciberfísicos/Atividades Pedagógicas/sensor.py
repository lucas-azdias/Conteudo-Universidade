#!/usr/bin/env python3
import socket
import struct
import sys
from multiprocessing import Process

def mostraip():
    hostname = socket.gethostname()
    hostip = socket.gethostbyname(hostname)
    print('host: {} ip: {}'.format(hostname, hostip))

def receptor(host, porta, id):
    print(id, ' foi iniciado')
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        s.bind((host,porta))
    except:
        print('erro de bind')

    while True:
        data, addr = s.recvfrom(1024)
        print(id, ': ' , addr, ' enviou ', data)
        s.sendto(id.encode() , addr )

if __name__ == '__main__':
    print("======= SENSOR ============")
    mostraip()
    Process(target=receptor, args=('',9999,'portaria')).start()
    Process(target=receptor, args=('127.0.0.2', 9999,'sala')).start()
    Process(target=receptor, args=('127.0.0.3', 9999,'quarto')).start()
    Process(target=receptor, args=('127.0.0.4', 9999,'cozinha')).start()

