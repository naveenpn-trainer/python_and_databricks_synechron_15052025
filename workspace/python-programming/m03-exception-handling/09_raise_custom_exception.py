from custom_exceptions import InvalidAgeExceptionWithLog


if __name__ == '__main__':
    try:
        age = int(input("Enter your cage"))
        if age<=18:
            raise InvalidAgeExceptionWithLog(age)
        else:
            print("Eligible to vote")

    except InvalidAgeExceptionWithLog as ex:
        print("Exception occurred: ",ex)