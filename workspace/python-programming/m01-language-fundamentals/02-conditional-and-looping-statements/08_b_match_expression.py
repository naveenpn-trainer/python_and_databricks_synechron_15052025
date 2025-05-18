age = int(input("Enter age"))

match age:
    case age if age < 0:
        print("Invalid Age")
    case age if age < 13:
        print("Child")
    case age if age < 18:
        print("Teen age")
    case age if age < 65:
        print("Adult")
    case _:
        print("Senior")