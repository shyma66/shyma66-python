def divide(numerator, denominator):
    # enter your code
    try:
        result= numerator / denominator
        return f"Result is {result}"
    except ZeroDivisionError:
        return f"Oops, {numerator}/{denominator}, division by zero is error!!!"
    except TypeError:
        return "Value Error! You did not enter a number!"

print(divide(4, 8))
print(divide(-1, 4))
print(divide(8, 0))
print(divide(-8, -2))
print(divide("9", 3))

print(divide("avr", 5))