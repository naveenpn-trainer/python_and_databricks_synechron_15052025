D5 = dict([("apples","red"),("oranges","orange")],grapes="green")
print(D5)

print("items()")
for k,v in D5.items():
    print(k,v)


print("values()")
for v in D5.values():
    print(v)

print("keys()")
for k in D5.keys():
    print(k)

print("----")
for k in D5:
    print(k)

# D = {"k1":[1,2,3]}