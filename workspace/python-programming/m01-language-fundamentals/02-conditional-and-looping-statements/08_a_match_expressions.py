role = input("Enter your role (admin, editor, viewer)")
# if role == "admin":
#     print("You have full access")
# elif role == "editor":
#     print("You can modify the content")
# elif role == "view":
#     print("You can only view the content")
# else:
#     print("Invalid role")
#
match role:
    case "admin" | "superadmin":
        print("You have full access")
    case "view":
        print("You can only view the content")
    case "editor":
        print("You can modify the content")
    case _:
        print("Invalid role")