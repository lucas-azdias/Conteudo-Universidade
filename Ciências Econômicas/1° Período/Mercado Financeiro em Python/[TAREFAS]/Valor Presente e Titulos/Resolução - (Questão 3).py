vp = 0 #Valor presente
vf = 2000 #Valor futuro / Valor de face

i = 0.04 #Taxa de juros / Taxa de desconto
tc = 0.02 #Taxa do cupom
c = tc * vf #Valor do cupom
t = 5 #Tempo

index = 1

while(index <= t):
    vp += c / (1 + i)**index
    index += 1

vp += vf / (1 + i)**t

print("Valor presente: ", vp)

'''

Resposta:
    3. $ 1821.93

'''