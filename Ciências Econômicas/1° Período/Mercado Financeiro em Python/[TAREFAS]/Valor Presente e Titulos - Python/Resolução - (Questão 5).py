#Calcula o valor futuro
def calc_vf(vp, i, t):
    return vp * (1 + i) ** t

#Calcula o valor presente
def calc_vp(vf, i, t):
    return vf / (1 + i) ** t

#Calcula o preço unitário para um título de cupom-zero (apenas valor de face)
def calc_pu(vf, i, t):
    return calc_vp(vf, i, t)

'''

Resposta:
    5.a) def calc_vf(vp, i, t):
            return vp * (1 + i) ** t
    5.b) def calc_vp(vf, i, t):
            return vf / (1 + i) ** t
    5.c) def calc_pu(vf, i, t):
            return calc_vp(vf, i, t)

'''