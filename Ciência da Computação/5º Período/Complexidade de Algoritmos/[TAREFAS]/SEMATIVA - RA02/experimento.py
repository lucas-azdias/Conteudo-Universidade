from CA.SEMANA11.bubble_sort_interativo import Bubble_Sort_interativo_wapper
from CA.SEMANA11.bubble_sort_recursivo import bubble_sort__recursivo_wapper
from CA.SEMANA11.quick_sort_recursivo import quick_sort_recursivo_wapper
from CA.SEMANA11.quick_sort_random import quick_sort_recursivo_random_wapper
from CA.SEMANA11.merge_sort_interativo import Merge_Sort_interativo_wapper
from CA.SEMANA11.merge_sort_recursivo import merge_sort__recursivo_wapper
from CA.SEMANA11.merge_sort_recursivo_random import merge_sort_recursivo_random_wapper
from CA.SEMANA11.select_sort_recursivo import select_sort_recursivo_wapper
from CA.SEMANA11.select_sort_recursivo_random import select_sort_recursivo_random_wapper
from CA.SEMANA11.sellSort_base_line import shellSort_Wapper
from CA.SEMANA11.gerador import gerar_dados_crescente
from CA.SEMANA11.gerador import gerar_dados_random
from CA.SEMANA11.gerador import gerar_dados_decrescente
from CA.SEMANA11.gerador import agora
from CA.SEMANA11.gerador import dif_time

import sys


def execucao(X):
    D = []
    header = []

    # header.append("BS_ITER")
    # a = agora()
    # BS1 = Bubble_Sort_interativo_wapper(X.copy())
    # b = agora()
    # D.append(dif_time(b,a))

    header.append("BS_REC")
    a = agora()
    BS2 = bubble_sort__recursivo_wapper(X.copy())
    b = agora()
    D.append(dif_time(b,a))

    header.append("QS_REC")
    a = agora()
    QS1 = quick_sort_recursivo_wapper(X.copy())
    b = agora()
    D.append(dif_time(b,a))

    header.append("QS_RAND")
    a = agora()
    QS2 = quick_sort_recursivo_random_wapper(X.copy())
    b = agora()
    D.append(dif_time(b,a))

    # header.append("MS_ITER")
    # a = agora()
    # MS1 = Merge_Sort_interativo_wapper(X.copy())
    # b = agora()
    # D.append(dif_time(b,a))

    header.append("MS_REC")
    a = agora()
    MS2 = merge_sort__recursivo_wapper(X.copy())
    b = agora()
    D.append(dif_time(b,a))

    header.append("MS_RAND")
    a = agora()
    MS3 = merge_sort_recursivo_random_wapper(X.copy())
    b = agora()
    D.append(dif_time(b,a))

    header.append("SS_REC")
    a = agora()
    SS1 = select_sort_recursivo_wapper(X.copy())
    b = agora()
    D.append(dif_time(b,a))

    header.append("SS_RAND")
    a = agora()
    SS2 = select_sort_recursivo_random_wapper(X.copy())
    b = agora()
    D.append(dif_time(b,a))

    header.append("BASELINE")
    a = agora()
    BASE_LINE = shellSort_Wapper(X.copy())
    b = agora()
    D.append(dif_time(b,a))

    return D, header


def exec_experimento(name, func):
    print('\n' + name)
    for i in range(0, N, 1):
        x, header = execucao(func( (i + 1) * T ))

        if i == 0:
            header.insert(0, "NUM")
            print(";".join(header))

        c = len(x) - 1

        print((i + 1) * T, end=';')
        for j, y in enumerate(x):
            if (j < c):
                print(y, end=';')
            else:
                print(y, end='')
        print()



T = 100
N = 10

sys.setrecursionlimit(T * (N + 1))

exec_experimento("DADOS_DECRESCENTES", gerar_dados_decrescente)
exec_experimento("DADOS_CRESCENTES", gerar_dados_crescente)
exec_experimento("DADOS_ALEATÓRIOS", gerar_dados_random)
