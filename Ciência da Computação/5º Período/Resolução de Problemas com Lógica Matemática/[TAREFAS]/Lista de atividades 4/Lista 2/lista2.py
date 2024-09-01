import ttg

print("Lista 2")

print(f"""
Exercício 3
a)
{ttg.Truths(['a', 'b'], ['(~a) and b'])}

b)
{ttg.Truths(['a', 'b'], ['(~b) => (a or b)'])}

c)
{ttg.Truths(['a', 'c'], ['(c or a) = (~(~c))'])}

d)
{ttg.Truths(['a', 'b'], ['a or (a => b)'])}

e)
{ttg.Truths(['a', 'c', 'd'], ['(d or (~a)) => (~c)'])}

f)
{ttg.Truths(['a', 'b', 'c'], ['(~(a and b)) => (~(c or b))'])}
""")

print(f"""
Exercício 4
a)
{ttg.Truths(['p', 'q'], ['~q', '(p => ~q)', '~(p => ~q)'])}

b)
{ttg.Truths(['p', 'q', 'r'], ['~q', '~q and r', 'p = ~q and r'])}

c)
{ttg.Truths(['p', 'q'], ['~q', '~q and p', '~q and p or q', 'p or ~q', 'p => ~q and p or q', 'p => ~q and p or q = p or ~q'])}
""")
