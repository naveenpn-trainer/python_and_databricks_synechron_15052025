# L1 = [5,4,3,2,4,6,8,1]
# print(max(L1))
# print(min(L1))
# print(len(L1))
# print(sorted(L1, reverse=True))
#
#
# L1 = [5,4,3,2,4,6,8,1,3,2,2]
# L1 = list(set(L1))
# print(L1)
from itertools import zip_longest

L1 = [1,2,4,1]
L2 = [4,5,6,5]

for i, j in zip_longest(L1, L2):
    print(i, j)