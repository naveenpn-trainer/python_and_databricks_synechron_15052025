D1 = {"apples":"red","oranges":"orange"}
print(type(D1))

D2 = dict(apples="red",oranges="orange")
print(D2)

D3 = dict(D2,grapes="green")
print(D3)

D4 = dict([("apples","red"),("oranges","orange")])
print(D4)

D5 = dict([("apples","red"),("oranges","orange")],grapes="green")
print(D5)

