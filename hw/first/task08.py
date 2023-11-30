# #Task02 Fibonacci
#
# n = int(input("Please write your number "))
#
# x, y = 0, 1
# count = 0
#
# if n <= 0:
#    print("Please enter a positive integer " )
#
# elif n == 1:
#    print("Fibonacci sequence upto",n,": ")
#    print(x)
#
# else:
#    print("Fibonacci sequence:")
#    while count < n:
#        print(x , end=" | ")
#        nth = x + y
#        x = y
#        y = nth
#        count += 1

def fibonacci_numbers():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Example usage:
fibonacci_gen = fibonacci_numbers()

# Print the first 10 Fibonacci numbers
for i in range(10):
    print(next(fibonacci_gen))
