class A:
    def __init__(self, message):
        self.message = message
        print("A Constructor")
class B(A):
    pass

class InvalidAgeException(Exception):
    pass

class InvalidAgeExceptionEnhancedOne(Exception):
    def __init__(self, age):
        self.age = age
        if self.age <= 18:
            self.message = f"Age: {self.age} is below 18"
        else:
            self.message = f"Age: {self.age} is valid for voting"
        super().__init__(self.message)

class InvalidAgeExceptionWithLog(Exception):
    def __init__(self, age):
        self.age = age
        self.message = f"Age: {self.age} is below 18"
        self.log_message()
        super().__init__(self.message)

    def log_message(self):
        with open("output.txt", "a") as file:
            file.write(self.message+"\n")

    def get_message(self):
        return f"{self.message}, {self.age}"