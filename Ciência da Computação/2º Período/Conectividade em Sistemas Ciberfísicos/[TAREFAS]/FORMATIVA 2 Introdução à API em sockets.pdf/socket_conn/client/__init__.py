from socket_conn.tools import *
import socket

class client:

      bffersize = 32768 #32MB

      def __init__(self, myAdress, af, sockettype) -> None:
            printHeader("Iniciando o cliente...")
            self.myAdress = myAdress # Define o adress desse cliente -> (HOST[String], PORT[int]) (Obs.: Portas abaixo de 1023 exigem permissão de root)
            self.af = af # Define o Adress Family (IPV4, IPV6, ...)
            self.sockettype = sockettype # Define o tipo de Socket (TCP/Stream, UDP/Datagram, IP/RAW)

            try:
                  # Cria um Socket inical baseado no IPV4 (Adress Family INET) e no TCP (Stream)
                  self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

                  # Solicita um porta de transporta ao SO
                  self.socket.bind(myAdress)
            except Exception as erro:
                  printError("Erro na inicialização do cliente", erro)
                  exit()


      def connect(self, adress):
            # Tenta conectar com o servidor no endereço adress
            printHeader(f"Conectando com {adress[0]} na porta {adress[1]}...")
            try:
                  self.socket.connect(adress)
            except Exception as erro:
                  printError(f"Não foi possível a conexão com {adress[0]} na porta {adress[1]}", erro)
            else:
                  printSucess(f"Conectado com sucesso com {adress[0]} na porta {adress[1]}")


      def close(self):
            # Finaliza o cliente
            printHeader("Encerrando cliente...")
            try:
                  self.socket.close()
            except Exception as erro:
                  printError("Erro ao encerrar o cliente", erro)
            else:
                  printSucess("Cliente encerrado com sucesso")
      
      
      def sendBytes(self, bytes):
            # Envia um array de bytes
            printHeader("Enviando bytes...")
            try:
                  tam = self.socket.send(bytes)
            except Exception as erro:
                  printError("Erro no envio de informação", erro)
            else:
                  printSucess(f"Enviados {tam} bytes com sucesso")

      
      def recvBytes(self):
            # Recebe um array de bytes
            printHeader("Recebendo bytes...")
            data = bytes()
            try:
                  data = self.socket.recv(self.bffersize)
            except Exception as erro:
                  printError("Erro no recebimento de informação", erro)
            else:
                  printSucess("Bytes recebidos com sucesso")
            return data
