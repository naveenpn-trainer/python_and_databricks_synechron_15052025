# D1 = {"apples":"red","oranges":"orange"}
# print(type(D1))
#
# # print(D1["grapes"])
# print(D1.get("apples"))
# print(D1.get("grapes"))
# print(D1.get("grapes","NOT DEFINED"))
D = {}
while True:
    key = input("Enter Key")
    value = input("Enter value")
    D[key]= value
    print(D)