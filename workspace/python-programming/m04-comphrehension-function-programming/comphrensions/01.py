L = list(range(1,11))
print(L)
E = []
for e in L:
    e+=1
    E.append(e)
print(E)

E = [e+1 for e in L]
print(E)


