from socket_conn.server import *
from socket_conn.client import *
from socket_conn.tools import *
import socket

def main():

      #Servidor
      myAdress = ('192.168.18.13', 9999)

      serv = server(myAdress, socket.AF_INET, socket.SOCK_STREAM)

      serv.awaitConn()

      text = ""
      print("\nDigite o texto a ser enviado:")
      while True:
            typed = input()
            if typed != "":
                  text += typed + "\n"
                  continue
            break
      serv.sendBytes(dataInBytes(text))

      # import json
      # data = bytesInData(serv.recvBytes())
      # print(data)

      serv.closeConn()
      serv.close()

      #Cliente
      # myAdress = ('192.168.18.16', 9999)
      # servAdress = ('192.168.18.13', 9999)

      # clnt = client(myAdress, socket.AF_INET, socket.SOCK_STREAM)

      # clnt.connect(servAdress)

      # data = bytesInData(clnt.recvBytes())
      # print(data)

      # clnt.close()


if __name__ == "__main__":
      main()
