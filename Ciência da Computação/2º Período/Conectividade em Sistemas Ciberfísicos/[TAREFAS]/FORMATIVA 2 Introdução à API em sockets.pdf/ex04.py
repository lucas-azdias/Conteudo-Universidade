import socket
import json

def main():
      mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      porta = int(input("Porta de origem: "))
      mySocket.bind(('192.168.18.13', porta))
      #mySocket.settimeout(10)

      mySocket.connect(("192.168.18.16", 9999))

      text = ""
      print("Digite o texto para ser enviado:")
      while True:
            line = input()
            if line != "":
                  text += line + "\n"
                  continue
            break
      mySocket.send(bytes(json.dumps([text]), "utf-8"))
      
      mySocket.close()


if __name__ == "__main__":
      main()
