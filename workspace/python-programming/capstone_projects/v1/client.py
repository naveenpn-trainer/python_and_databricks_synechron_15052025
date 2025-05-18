import sys
def m1():
    print("m1()")

print(__name__)

MENU = '''
1. Add a book
2. Mark a book as red
3. Delete a book
4. List all books
q. Quit`
'''
BOOKS = []
while True:
    print(MENU)
    user_input = input("Enter your choice")
    if user_input =="1":
        name = input("Enter name")
        author = input("Enter author")
        BOOKS.append({'name':name,'author':author,'is_read':False})
    elif user_input =="4":
        for book in BOOKS:
            print(f"Name: {book['name']},Author: {book['author']},Is Read: {book['is_read']}")
    elif user_input =="3":
        name = input("Enter name")
        for book in BOOKS:
            if book['name'] == name:
                BOOKS.remove(book)
                break
    elif user_input == "2":
        name = input("Enter name")
        for book in BOOKS:
            if book['name'] == name:
                book['is_read'] = True
                break

    elif user_input =="q":
        sys.exit(1)
