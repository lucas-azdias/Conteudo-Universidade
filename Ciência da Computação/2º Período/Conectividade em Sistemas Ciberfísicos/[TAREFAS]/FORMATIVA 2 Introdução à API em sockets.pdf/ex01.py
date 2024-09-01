import socket
import json

def main():
      mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      mySocket.bind(('192.168.18.13', 9999))
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

            text = ""
            print("Digite o texto para ser enviado:")
            while True:
                  line = input()
                  if line != "":
                        text += line + "\n"
                        continue
                  break
            conn.send(bytes(json.dumps([text]), "utf-8"))
            conn.close()
      mySocket.close()


if __name__ == "__main__":
      main()
