data = [
    {"vf": 7500, #Valor futuro
     "i": 0.15, #Taxa de juros / Taxa de desconto
     "t": 5}, #Tempo
    {"vf": 13000, #Valor futuro
     "i": 0.03, #Taxa de juros / Taxa de desconto
     "t": 10}, #Tempo
    {"vf": 100000000, #Valor futuro
     "i": 0.20, #Taxa de juros / Taxa de desconto
     "t": 35} #Tempo
    ]

for index in range(len(data)):
    vf = data[index].get("vf")

    i = data[index].get("i")
    t = data[index].get("t")

    data[index]["vp"] = vf / (1 + i) ** t #Valor presente

print(f"a) Valor presente: {data[0].get('vp'):.2f}",
    f"\nb) Valor presente: {data[1].get('vp'):.2f}",
    f"\nc) Valor presente: {data[2].get('vp'):.2f}")

'''

Resposta:
    2.a) Valor presente: 3728.83 
    2.b) Valor presente: 9673.22
    2.c) Valor presente: 169299.78

'''