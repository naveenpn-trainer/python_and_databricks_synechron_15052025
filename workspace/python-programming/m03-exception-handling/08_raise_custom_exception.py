from custom_exceptions import InvalidAgeExceptionEnhancedOne


if __name__ == '__main__':
    try:
        age = int(input("Enter your age"))
        if age<=18:
            raise InvalidAgeExceptionEnhancedOne(age)
        else:
            print("Eligible to vote")

    except InvalidAgeExceptionEnhancedOne as ex:
        print("Exception occurred: ",ex)