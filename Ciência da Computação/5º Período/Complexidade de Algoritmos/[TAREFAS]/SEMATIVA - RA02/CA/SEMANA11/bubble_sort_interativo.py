# Iterative sort
def Bubble_Sort(S):
    n = len(S)
    
    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if S[j] > S[j+1]:
                S[j], S[j+1] = S[j+1], S[j]
                swapped = True
        if (swapped == False):
            break


def Bubble_Sort_interativo_wapper(A):
    return Bubble_Sort(A)

#X = [58, 30, 97, 21, 81, 35, 48, 59, 24, 2, -1]
#print('ANTES',X)
#QQ = Bubble_Sort_interativo_wapper(X)
#print('DEPOIS',QQ)
