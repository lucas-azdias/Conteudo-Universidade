import urequests
from wifi_lib import conecta

wifi_ssid = 'Wokwi-GUEST'
wifi_password = ''

print("Conectando...")
station = conecta(wifi_ssid, wifi_password)
if not station.isconnected():
    print("Não conectado!...")
else:
    print("Conectado!...")
