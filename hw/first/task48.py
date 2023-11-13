def my_decorator(func):
    def wrapper():
        print("Действие перед вызовом функции")
        func()
        print("Действие после вызова функции")
    return wrapper

@my_decorator
def say_hello():
    print("Привет!")

# Вызов функции с декоратором
say_hello()
