DU = 252

vf = 1000000 #Valor futuro / Valor de face

t = 504/DU #Tempo

i_default = 0.11 #Taxa de juros / Taxa de desconto

data = [
    [0.07],
    [0.09],
    [0.11],
    [0.13],
    [0.15],
    [0.17]
    ]

vp_default = vf / (1 + i_default) ** t #Valor presente / Preço unitário

print(f"|__i__|__Preço_unitário__|")

for index in range(len(data)):
    data[index].append(vf / (1 + data[index][0]) ** t) #Valor presente / Preço unitário

    print(f"|{data[index][0]:.2f}_|{str(round(data[index][1], 2)).rjust(18, '_')}|")

'''

Resposta:
    4. |__i__|__Preço_unitário__|
	   |0.07_|_________873438.73|
	   |0.09_|_________841679.99|
	   |0.11_|_________811622.43|
	   |0.13_|_________783146.68|
	   |0.15_|_________756143.67|
	   |0.17_|_________730513.55|

'''