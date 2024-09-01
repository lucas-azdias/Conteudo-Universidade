import ttg

print("Lista 1")

print(f"""
Exercício 1
a)
{ttg.Truths(['p'], ['~p'])}

b)
{ttg.Truths(['p', 'q'], ['p and q'])}

c)
{ttg.Truths(['p', 'q'], ['p or q'])}

d)
{ttg.Truths(['p', 'q'], ['q = p'])}

e)
{ttg.Truths(['p', 'q'], ['p => (~q)'])}

f)
{ttg.Truths(['p', 'q'], ['p or (~q)'])}

g)
{ttg.Truths(['p', 'q'], ['(~p) and (~q)'])}

h)
{ttg.Truths(['p', 'q'], ['p = (~q)'])}

i)
{ttg.Truths(['p', 'q'], ['(p and (~q)) => p'])}
""")

print(f"""
Exercício 2
a)
{ttg.Truths(['p', 'q'], ['(~p) and q'])}

b)
{ttg.Truths(['p', 'q'], ['p and (~q)'])}

c)
{ttg.Truths(['p', 'q'], ['(~p) and (~q)'])}

d)
{ttg.Truths(['p', 'q'], ['((~p) or p) and q'])}
""")

print(f"""
Exercício 3
a)
{ttg.Truths(['p', 'q'], ['q = p'])}

b)
{ttg.Truths(['p', 'q'], ['~(~p)'])}

c)
{ttg.Truths(['p', 'q'], ['~((~p) and (~q))'])}
""")

print(f"""
Exercício 4
a)
{ttg.Truths(['p', 'q', 'r'], ['(p or q) and (~r)'])}

b)
{ttg.Truths(['p', 'q', 'r'], ['(p and q) or (~(p and r))'])}

c)
{ttg.Truths(['p', 'q', 'r'], ['~(p and (~r))'])}

d)
{ttg.Truths(['p', 'q', 'r'], ['~((q or r) and (~p))'])}
""")

print(f"""
Exercício 5
a)
{ttg.Truths(['p', 'q', 'r'], ['(~(p and q)) or (~q)'])}

b)
{ttg.Truths(['p', 'q', 'r'], ['(~(p or q)) and r'])}

c)
{ttg.Truths(['p', 'q', 'r'], ['(~r) => (p and (~q))'])}

d)
{ttg.Truths(['p', 'q', 'r'], ['~((~(p and q)) and (r and p))'])}
""")
