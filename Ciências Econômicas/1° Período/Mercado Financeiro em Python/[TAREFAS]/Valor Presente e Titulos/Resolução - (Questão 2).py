vp = 0 #Valor presente
vf = 100 #Valor futuro / Valor de face

i = 0.06 #Taxa de juros / Taxa de desconto
tc = 0.05 #Taxa do cupom
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
    2. € 92.64

'''