print("Hello! \nYou are in the calculator now")

x = float(input("Write your first_kurs number\n->"))
action = (input("Write your action (+; -; *; **; /; //; %.)\n->"))
y = float(input("Write your second_kurs number\n->"))

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