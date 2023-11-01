class Human:
    def __init__(self,name):
        self.name = name
    def message(self):
        return f"Welcome {self.name}"
    @classmethod
    def information_message(cls):
        return "It is a species of Homosapiens."

    @staticmethod
    def arbitrary_message():
        return "This is an arbitrary message."

first_name = Human(input("Enter your name -> "))
second_name = Human(input("Enter your name -> "))

print(first_name.message())  # Output: "Hello, my name is Alice. Welcome!"
print(second_name.message())  # Output: "Hello, my name is Bob. Welcome!"

print(Human.information_message())  # Output: "I am a species of Homosapiens."
print(Human.arbitrary_message())