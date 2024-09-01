data = [
    {"vp": 1000, #Valor presente
     "i": 0.12, #Taxa de juros / Taxa de desconto
     "t": 10}, #Tempo
    {"vp": 100000, #Valor presente
     "i": 0.07, #Taxa de juros / Taxa de desconto
     "t": 35}, #Tempo
    {"vp": 100000, #Valor presente
     "i": 0.09, #Taxa de juros / Taxa de desconto
     "t": 720/12} #Tempo
    ]

for index in range(len(data)):
    vp = data[index].get("vp")

    i = data[index].get("i")
    t = data[index].get("t")

    data[index]["vf"] = vp * (1 + i) ** t #Valor futuro

print(f"a) Valor futuro: {data[0].get('vf'):.2f}",
    f"\nb) Valor futuro: {data[1].get('vf'):.2f}",
    f"\nc) Valor futuro: {data[2].get('vf'):.2f}")

'''

Resposta:
    1.a) Valor futuro: 3105.85
    1.b) Valor futuro: 1067658.15
    1.c) Valor futuro: 17603129.20

'''