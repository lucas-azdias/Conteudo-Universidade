#!/usr/bin/env python3

import socket
import sys
import time

HOST = '127.0.0.1' # IP do servidor
PORT = 9999 # Porta do servidor

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	s.connect((HOST, PORT))
	time.sleep(60)
except:
	print('# erro de conexao')
	sys.exit()