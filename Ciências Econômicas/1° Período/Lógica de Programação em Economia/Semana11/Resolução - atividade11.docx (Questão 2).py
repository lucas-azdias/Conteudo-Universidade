def vp_fluxo(fluxo_caixa, i):
    vp = 0
    for p in range(len(fluxo_caixa)):
        vp += fluxo_caixa / (1 + i) ** p
    return vp

def vp(vf, i, p):
    return vf / (1 + i) ** p

print("\n| Calculador de indíce de lucratividade |\n")

#Head
n = int(input("Período do fluxo de caixa: "))
inFluxo = list()
for p in range(n):
    inFluxo.append(abs(float(input(f"Entrada no caixa no período {p + 1}: "))))
outFluxo = list()
for p in range(n):
    outFluxo.append(abs(float(input(f"Saída no caixa no período {p + 1}: "))))
i = float(input("Taxa de desconto do valor futuro: ").replace(",", "."))

inVp = 0
outVp = 0
iLucro = 0

#Body
for p in range(n):
#    delta = inFluxo[p] - outFluxo[p]
#    if(delta > 0):
#        inVp += vp(delta, i, p)
#    elif(delta < 0):
#        outVp += vp(delta, i, p)
    inVp += vp(inFluxo[p], i, p)
    outVp += vp(outFluxo[p], i, p)

iLucro = inVp / outVp

print(f"\nO índice de lucratividade para o fluxo de caixa dado é {iLucro * 100:.2f}%")
