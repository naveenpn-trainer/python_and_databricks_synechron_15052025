def connect(**kwargs):
    if kwargs['user'] == "admin" and kwargs["password"] =="qwerty":
        print("Access granted")

connect(user="root", password="qwerty",ssl="True")