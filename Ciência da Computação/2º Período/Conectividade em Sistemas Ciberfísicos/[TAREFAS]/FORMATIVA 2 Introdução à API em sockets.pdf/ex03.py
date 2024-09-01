import socket
import json

def main():
      mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      porta = int(input("Porta de origem: "))
      mySocket.bind(('192.168.18.13', porta))
      mySocket.listen(5)
      #mySocket.settimeout(10)

      while True:
            print("\nNew connection")
            try:
                  conn, adrrs = mySocket.accept()
            except:
                  break
            else:
                  print(f"Conexão de {adrrs[0]}:{adrrs[1]}")

            while True:
                  print(conn.recv(1024).decode("utf-8"))
            #conn.close()
      mySocket.close()


if __name__ == "__main__":
      main()
