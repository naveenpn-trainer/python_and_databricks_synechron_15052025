from custom_exceptions import InvalidAgeException

try:
    age = int(input("Enter your age"))
    if age<18:
        raise InvalidAgeException(f"Entered age {age}:  is below 18")
    else:
        print("Eligible to vote")
except InvalidAgeException as ex:
    print("Exception occurred: ",ex)