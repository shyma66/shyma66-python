def check_odd_even(number):
    try:
        if isinstance(number, int):
            if number % 2 == 0:
                return "Entered number is even"
            else:
                return "Entered number is odd"
        else:
            return "Entered number is not an integer"
    except TypeError:
        return "You entered not a number."

# Example usage:
number = input("Enter a number: ")
try:
    number = int(number)
    result = check_odd_even(number)
    print(result)
except ValueError:
    print("Invalid input. Please enter an integer.")