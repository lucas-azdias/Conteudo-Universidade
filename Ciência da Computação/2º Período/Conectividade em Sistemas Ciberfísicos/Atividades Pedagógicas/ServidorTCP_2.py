# ServidorTCP.py
#!/usr/bin/env python3

import socket
import sys

HOST = '127.0.0.1'  # localhost = esta máquina

PORT = int(input('Qual porta para o Server?'))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((HOST, PORT))
except:
   print('# erro de bind')
   sys.exit()

s.listen(5)

print('aguardando conexoes em ', PORT)

while True:
	conn, addr = s.accept()
	print('recebi uma conexao de ', addr)
	print('o cliente encerrou')
	conn.close()



