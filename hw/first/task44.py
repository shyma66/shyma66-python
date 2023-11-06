class InputError(Exception):
    def __init__(self, description):
        self.data = description

def check(text):
    if not isinstance(text, str):
        raise InputError("Type text error")
    if len(text) < 3:
        raise InputError("Short text error")
    if len(text) > 15:
        raise InputError("Long text error")
    return True
def test_input(text):
    try:

        print(check(text))
    except InputError as e:
        print(f"InputError: {e.data}")

# Example usage:
test_input("Valid Text")  # Should print "Input is valid."
test_input("Sh")          # Should print "InputError: Short text error"
test_input("VeryLongTextThatExceedsTheMaxLength")  # Should print "InputError: Long text error"
test_input(123)           # Should print "InputError: Type text error"
test_input("Hello world")