#Head
num = 0
limit = 0

#Body
while True:

    num = int(input("Número da tabuada: "))    
    
    if num == -1:
        print("Programa encerrado")
        break

    limit = int(input("Número limite na tabuada: "))

    print(f"\n--- Tabuada do {num} ---")

    for i in range(1, limit + 1):
        print(f"    {num} × {i} = {num * i}")

    print("")
