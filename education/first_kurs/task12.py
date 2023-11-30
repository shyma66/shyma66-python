def largest_number():
    if number1 > number2:
        return number1
    else:
        return number2



number1 = int(input("Enter the first_kurs number: "))
number2 = int(input("Enter the second number: "))

result = largest_number()
print(result,"is the largest number.")