L = list(range(1,11))
print(L)
# L[-1]= 11
# print(L[0:3])
# L[0:3] = [11,12,13]
# print(L)
#


del L[-1]
print(L)
del L[0:4]
print(L)

L.remove(5)
print(L)
L.pop(1)
print(L)