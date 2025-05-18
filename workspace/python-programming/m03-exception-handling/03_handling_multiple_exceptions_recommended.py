def calculate_quotient(numerator, denominator):
    return numerator/denominator

def get_last_value(lst):
    return  lst[-1]

if __name__ == '__main__':
    try:
        numerator = int(input("Enter numerator"))
        denominator = int(input("Enter denominator"))
        result = calculate_quotient(numerator, denominator)
        print(f"{numerator}/{denominator}= {result}")
    except (ZeroDivisionError, ValueError) as ex:
        if isinstance(ex, ZeroDivisionError):
            print("Enter denominator greater than zero")
        elif isinstance(ex, ValueError):
            print("Enter only integers")

    print(get_last_value([1,4,5]))