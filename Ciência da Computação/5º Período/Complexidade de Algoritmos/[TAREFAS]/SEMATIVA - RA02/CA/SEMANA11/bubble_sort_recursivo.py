def bubble_sort(A, n):
    if n == 1:
        return
    
    for i in range(n-1):
        if A[i] > A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]
    
    bubble_sort(A, n-1)

def bubble_sort__recursivo_wapper(A):
    bubble_sort(A, len(A))
    return A

# X = [58, 30, 97, 21, 81, 35, 48, 59, 24, 2, -1]
# print('ANTES',X)
# QQ = bubble_sort__recursivo_wapper(X)
# print('DEPOIS',QQ)
