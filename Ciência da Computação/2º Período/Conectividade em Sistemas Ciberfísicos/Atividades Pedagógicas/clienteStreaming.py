#!/usr/bin/env python3
import socket
import struct
import sys
from multiprocessing import Process

def mostraip():
    hostname = socket.gethostname()
    hostip = socket.gethostbyname(hostname)
    print('host: {} ip: {}'.format(hostname, hostip))  

def receptor(host, group, porta, id):
    print(id, ' foi iniciado')
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        s.bind((host,porta))
        mreq = struct.pack("4sl", socket.inet_aton(group), socket.INADDR_ANY)
        s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)      
    except:
        print('erro de bind')

    while True:
        data, addr = s.recvfrom(1024)
        print(id, ': ' , addr, ' enviou ', data)
        s.sendto(id.encode() , addr )

if __name__ == '__main__':
    mostraip()
    Process(target=receptor, args=('','224.1.2.3',9999,'cliente 1 streaming 1')).start()
    Process(target=receptor, args=('','224.1.2.3',9999,'cliente 2 streaming 1')).start()
    Process(target=receptor, args=('','224.1.2.4',9999,'cliente 3 streaming 2')).start()
    Process(target=receptor, args=('','224.1.2.3',9999,'cliente 4 streaming 1')).start()
    Process(target=receptor, args=('','224.1.2.4',9999,'cliente 5 streaming 2')).start()
    Process(target=receptor, args=('','224.1.2.4',9999,'cliente 6 streaming 2')).start()
    Process(target=receptor, args=('','224.1.2.3',9999,'cliente 7 streaming 1')).start()
    Process(target=receptor, args=('','224.1.2.4',9999,'cliente 8 streaming 2')).start()