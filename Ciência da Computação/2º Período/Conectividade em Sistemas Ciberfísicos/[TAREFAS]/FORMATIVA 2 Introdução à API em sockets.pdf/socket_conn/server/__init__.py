from socket_conn.tools import *
import socket

class server:

      n = 5
      timeout = 10
      bffersize = 32768 #32MB

      def __init__(self, myAdress, af, sockettype) -> None:
            printHeader("Iniciando o servidor...")
            self.myAdress = myAdress # Define o adress desse servidor -> (HOST[String], PORT[int]) (Obs.: Portas abaixo de 1023 exigem permissão de root)
            self.af = af # Define o Adress Family (IPV4, IPV6, ...)
            self.sockettype = sockettype # Define o tipo de Socket (TCP/Stream, UDP/Datagram, IP/RAW)

            try:
                  # Cria um Socket inical baseado no IPV4 (Adress Family INET) e no TCP (Stream)
                  self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

                  # Solicita um porta de transporta ao SO
                  self.socket.bind(myAdress)

                  # Autoriza o SO a receber até n conexões pendentes
                  self.socket.listen(self.n)

                  # Define o timeout de espera por uma conexão
                  self.socket.settimeout(self.timeout)
            except Exception as erro:
                  printError(f"Erro na inicialização do servidor", erro)
                  exit()


      def awaitConn(self):
            # Aguarda e registra uma conexão conn de um endereço adrss
            printHeader(f"Aguardando requisição em {self.myAdress[0]}:{self.myAdress[1]}")
            try:
                  self.conn, self.adrss = self.socket.accept()
            except Exception as erro:
                  printError(f"Erro na inicialização do servidor", erro)
            else:
                  printSucess(f"Conexão recebida de {self.adrss[0]}:{self.adrss[1]}")


      def closeConn(self):
            # Finaliza a conexão
            printHeader("Encerrando conexão...")
            try:
                  self.conn.close()
            except Exception as erro:
                  printError("Erro ao encerrar conexão", erro)
            else:
                  printSucess("Encerrado com sucesso")


      def close(self):
            # Finaliza o servidor
            printHeader("Encerrando servidor...")
            try:
                  self.socket.close()
            except Exception as erro:
                  printError("Erro ao encerrar o servidor", erro)
            else:
                  printSucess("Servidor encerrado com sucesso")

      
      def sendBytes(self, bytes):
            # Envia um array de bytes
            printHeader("Enviando bytes...")
            try:
                  tam = self.conn.send(bytes)
            except Exception as erro:
                  printError("Erro no envio de informação", erro)
            else:
                  printSucess(f"Enviados {tam} bytes com sucesso")

      
      def recvBytes(self):
            # Recebe um array de bytes
            printHeader("Recebendo bytes...")
            data = bytes()
            try:
                  data = self.conn.recv(self.bffersize)
            except Exception as erro:
                  printError("Erro no recebimento de informação", erro)
            else:
                  printSucess("Bytes recebidos com sucesso")
            return data
