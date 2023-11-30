# def star(tag):
#     def inner(*args ,**kwargs):
#         print("*" * 30)
#         tag(*args,**kwargs)
#         print("*" * 30)
#     return inner
#
# @star
# def printer(msg):
#     print(msg)
# printer("Hello")

def add_tag(tag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{tag}{result}{tag}"
        return wrapper
    return decorator

# Example usage:
@add_tag("<strong>")
def get_message():
    return "Hello, World!"

# Output:
print(get_message())

