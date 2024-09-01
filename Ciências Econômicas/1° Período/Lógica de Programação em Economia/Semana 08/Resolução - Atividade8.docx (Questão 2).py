#Head
sum = 0

#Body
sum += 1 #Já somado 1 (1 é o primeiro múltiplo)
for i in range(3, 500, 3):
    sum += i

print("A soma de todos os múltiplos de 3 até 500 é", sum)