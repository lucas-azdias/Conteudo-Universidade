import ttg

print("Lista 3")

print(f"""
Exercício 1
{ttg.Truths(['T', 'D', 'L', 'S'], ['(T and D) and L => S', '~T or ~D or ~L or S'])}
""")

print(f"""
Exercício 2
{ttg.Truths(['M', 'A', 'B'], ['(M and ~A) => B', '~M or A or B'])}
""")

print(f"""
Exercício 3
{ttg.Truths(['A', 'B', 'R'], ['(A and B) or (A and R)', 'A and (B or R)'])}
""")
