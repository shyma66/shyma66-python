import re

def log_in(password):

    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@]).{6,16}$"

    if re.match(pattern, password):
        return True
    else:
        print("""--<Error>--\nAt least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9].
At least 1 character from [$#@].
Minimum length 6 characters.
Maximum length 16 characters.""")
        return False

while True:
    user_password = input("Enter your password: ")

    if log_in(user_password):
        print("Correct password.")
        break
    else:
        print("Invalid password.")
        print(">", user_password, "<")