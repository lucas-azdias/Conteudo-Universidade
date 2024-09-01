#Head
num = 5
limit = int(input("Número limite na tabuada: "))

#Body
print(f"\n--- Tabuada do {num} ---")

for i in range(1, limit + 1):
    print(f"    {num} × {i} = {num * i}")