L = [1,2,3,4]
print(type(L))

L = list([1,2,3,4,"A",23.0,2,-100,True])
print(type(L[-1]))
print(type(L))
print(L)

print(L[-1])

print(L[0::2])

'''
There are two ways to traverse a list
1. element wise
2. index wise
'''
L = [12,13,12,3,4,5]
print("element wise")
for e in L:
    print(e)
print("index wise")
for i in range(0, len(L)):
    print(L[i])