a = int(input("Enter a temperature in Celsius "))

Fahrenheit = (a * 9/5) + 32

match a :
    case a if a < -273.15 :
        print("ERROR\n-273.15°C The lowest possible temperature in the universe!")
    case _ :
        print(int(Fahrenheit),"°F")
