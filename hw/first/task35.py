class MyClass:
    """THIS IS """
    a = 10
    def func(self):
        print("HELLO")

print(MyClass.a)
print(MyClass.__doc__)
# print(MyClass().func())
first = MyClass()
# print(first.func())

MyClass().func()
