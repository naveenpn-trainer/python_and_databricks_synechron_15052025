L = list(range(1,10))
print(L)
E=[]
for e in L:
    if e%2==0:
        E.append(e+1)
    else:
        E.append(e+2)
print(E)


L=list(range(1,11))
E=[e+1 if e%2==0 else e+2 for e in L ]
print(E)