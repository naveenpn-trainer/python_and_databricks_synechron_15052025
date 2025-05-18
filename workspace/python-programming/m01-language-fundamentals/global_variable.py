#  Global Variable
counter = 0

def increment_counter():
    global counter
    counter += 1
    print(counter)

def decrement_counter():
    global  counter
    counter -= 1
    print(counter)

increment_counter()
increment_counter()
decrement_counter()