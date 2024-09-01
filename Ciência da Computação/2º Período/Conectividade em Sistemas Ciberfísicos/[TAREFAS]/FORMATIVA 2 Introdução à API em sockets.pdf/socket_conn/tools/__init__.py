default_encoding = "utf-8"

def printHeader(prompt):
      from time import sleep
      print(f"\n\033[1;33m{prompt}\033[m")
      sleep(0.5)


def printSucess(prompt):
      from time import sleep
      print(f"\033[1;34m{prompt}\033[m")
      sleep(0.5)


def printError(prompt, erro=Exception()):
      from time import sleep
      try:
            print(f"\033[1;31m{prompt} ({erro.__class__.__name__}, {erro.args[0]})\033[m")
      except:
            print(f"\033[1;31m{prompt} (Não identificado, {None})\033[m")
      sleep(0.5)


def dataInBytes(data):
      from json import dumps
      data = dumps([data])
      return bytes(data, default_encoding)


def bytesInData(bytes):
      from json import loads
      bytes = loads(bytes.decode(default_encoding))
      return bytes[0]
