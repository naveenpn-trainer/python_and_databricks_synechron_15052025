
def missing_number(L):
    for i in range(len(L)-1):
        if L[i]+ 1 == L[i+1]:
            pass
        else:
            print(f"missing number {L[i]+1}")


L = [11, 12, 14, 15, 16, 17,-2]
L = sorted(L)
print(missing_number(L))

