#Obs.: O título tem cupom-zero (tc = 0; c = 0)

DU = 252

data = [
    {"vf": 25000, #Valor futuro (Valor de face)
     "i": 0.15, #Taxa de juros / Taxa de desconto
     "t": 500/DU}, #Tempo
    {"vf": 130000, #Valor futuro (Valor de face)
     "i": 0.03, #Taxa de juros / Taxa de desconto
     "t": 700/DU}, #Tempo
    {"vf": 1000000, #Valor futuro (Valor de face)
     "i": 0.11, #Taxa de juros / Taxa de desconto
     "t": 504/DU} #Tempo
    ]

for index in range(len(data)):
    vf = data[index].get("vf")

    i = data[index].get("i")
    t = data[index].get("t")
    
    data[index]["vp"] = vf / (1 + i) ** t #Valor presente (Preço unitário)

print(f"a) Preço unitário: {data[0].get('vp'):.2f}",
    f"\nb) Preço unitário: {data[1].get('vp'):.2f}",
    f"\nc) Preço unitário: {data[2].get('vp'):.2f}")

'''

Resposta:
    3.a) Preço unitário: 18945.57 
    3.b) Preço unitário: 119752.45 
    3.c) Preço unitário: 811622.43

'''