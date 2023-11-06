class MyError(Exception):
    # enter your code

    pass
def check_positive(number):
    try:
        number = float(number)
        if number > 0:
            return f"You input positive number: {number}"
        elif number < 0:
            return f"You input negative number: {number}. Try again."


    except ValueError :
        return f"Error type: ValueError!"

print(isinstance(check_positive("-235"), MyError))