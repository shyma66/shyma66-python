def check(login):
    # Convert the login to lowercase for case-insensitivity
    login = login.lower()

    # Define a list of valid roles
    valid_roles = ["admin", "employee"]

    # Split the login by "-" and "id" to extract the role and id parts
    for separator in ["-", "-id", "id"]:
        if separator in login:
            role_part, id_part = login.split(separator, 1)
            if role_part in valid_roles and id_part.isdigit():
                return True

    raise ValueError(f"incorrect login '{login}'")

# Test cases
correct_logins = [
    "admin-123",
    "employee-456",
    "admin-id789",
    "employee-id101",
]

incorrect_logins = [
    "abc",
    "admin-id-",
    "employee-xyz",
]

for login in correct_logins:
    try:
        check(login)
        print("checked successfully")
    except ValueError as e:
        print(f"checked not successfully with {login}")

for login in incorrect_logins:
    try:
        check(login)
        print("checked successfully")
    except ValueError as e:
        print(f"checked not successfully with {login}")
