vp = 0 #Valor presente
vf = 1000 #Valor futuro / Valor de face

i = 0.09 #Taxa de juros / Taxa de desconto
tc = 0.06 #Taxa do cupom
c = tc * vf #Valor do cupom
t = 10 #Tempo

index = 1

while(index <= t):
    vp += c / (1 + i)**index
    index += 1

vp += vf / (1 + i)**t

print("Valor presente: ", vp)

'''

Resposta:
    1.a) preço dos títulos cai
    1.b) preço dos títulos cai
    1.c) preço dos títulos cai

'''