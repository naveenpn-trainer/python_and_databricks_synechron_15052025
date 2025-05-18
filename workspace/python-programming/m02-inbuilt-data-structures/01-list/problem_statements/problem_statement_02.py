L = [1,2,3,[3,5,4],4,5,[5,4,6]]
print(isinstance(L[3], int))


class A:
    pass
class B:
    pass

obj = A()
print(isinstance(obj, B))