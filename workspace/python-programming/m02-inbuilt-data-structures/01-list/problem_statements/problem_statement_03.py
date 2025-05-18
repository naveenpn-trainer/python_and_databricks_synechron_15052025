L = [1,2,4,2,1,2,3,4]
# for i in range(len(L)-1):
#     print(L[i],L[i+1])
#

# L1=[1,2,3,4,5,6,7,8]
# flag=False
# for i in range(0,len(L1)):
#     if L1[i]< L1[i+1]:
#         flag = True
# if flag==True:
#     print("Asscendibng Order")
# else :
#     print("Descending Order")
#
def is_ascending(L):
    for i in range(len(L)-1):
        if L[i] > L[i+1]:
            return False
    return True

# print(is_ascending([1,2,3,4,5,6]))
# print(is_ascending([11,1,2,3,4,5,6]))
# print(is_ascending([2,3,4,5,6,1]))

x = 10
y = 10
# print(id(x))
# print(id(y))
# print(x==y)

L1 = [1,2,3]
L2 = [1,2,3]
print(id(L1))
print(id(L2))
print(L1 == L2)

def check(L1,L2):
    if len(L1) != len(L2):
        return False
    for i in range(len(L1)-1):
        if L1[i]!=L2[i]:
            return False
    return True

print(check(L1,L2))