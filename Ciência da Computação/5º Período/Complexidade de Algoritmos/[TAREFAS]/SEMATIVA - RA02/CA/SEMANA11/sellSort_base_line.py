
def shellSort(array, a):
    mid = a // 2
    while mid > 0:
        for i in range(mid, a):
            chave = array[i]
            j = i
            while j >= mid and array[j - mid] > chave:
                array[j] = array[j - mid]
                j -= mid
            array[j] = chave
        mid //= 2
    return array

def shellSort_Wapper(array):
    return shellSort(array, len(array))

#X = [58, 30, 97, 21, 81, 35, 48, 59, 24, 2, -1]
#print('ANTES',X)
#QQ = shellSort_Wapper(X)
#print('DEPOIS',QQ)
