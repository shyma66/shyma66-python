#Task03

# from math import factorial
factor = int(input("Your number >> " ))

# print("Factorial is", factorial(factor))
def factorial(n):
    return 1 if (n ==1 or n==0) else n * factorial(n -1)

print("Factorial of ", factor ,"is", factorial(factor))
