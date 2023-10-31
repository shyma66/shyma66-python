print("Hello! \nYou are in the calculator now")

x = float(input("Write your first number\n->"))
action = (input("Write your action (+; -; *; **; /; //; %.)\n->"))
y = float(input("Write your second number\n->"))

if action == '+':
    print(x + y )
elif action == '-':
    print(x - y)
elif action == '*':
    print(x * y)
elif action == '/':
    print(x / y)
elif action == '**':
    print(x ** y)
elif action == '//':
    print(x // y)
elif action == '%':
    print(x % y)
else:
    print("Error")