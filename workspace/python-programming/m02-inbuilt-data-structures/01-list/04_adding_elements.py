L = [2,3,4,6,7,8,9]
L.append(10)
print(L)
L.insert(3,5)
print(L)


L1 = [1,2,3]
L2 = [4,5,6]
# L1.append(L2)
# print(L1)
# print(len(L1))

L1.extend(L2)
print(L1)