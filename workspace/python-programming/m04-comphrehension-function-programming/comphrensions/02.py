L = list(range(1,11))
print(L)
E = []
for e in L:
    if e%2==0:
        E.append(e)
print(E)

E = [e for e in L if e%2==0]
print(E)