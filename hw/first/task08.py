#Task02

n = int(input("Please write your number"))

x, y = 0, 1
count = 0

if n <= 0:
   print("Please enter a positive integer")

elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(x)

else:
   print("Fibonacci sequence:")
   while count < n:
       print(x , end=" ")
       nth = x + y
       x = y
       y = nth
       count += 1

