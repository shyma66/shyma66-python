# first_kurs version
a = int(input("Enter a temperature in Celsius "))

Fahrenheit = (a * 9/5) + 32

match a :
    case a if a < -273.15 :
        print("ERROR\n-273.15°C The lowest possible temperature in the universe!")
    case _ :
        print(int(Fahrenheit),"°F")

#second_kurs version
def celsius_to_fahrenheit(temps):
    # enter you code
    celsius_temperatures = list(map(lambda x: (x * 9/5)+ 32, temps))
    return celsius_temperatures

celsius_temperatures = [0, 10, 20, 30, 40]
print(celsius_to_fahrenheit(celsius_temperatures))

#thirds version

def celsius_to_fahrenheit(temps):
    # enter you code
    celsius_temperatures = [(temp * 9 / 5) + 32 for temp in temps]
    return celsius_temperatures

celsius_temperatures = [-40, -30, -20, -10, 0]
print(celsius_to_fahrenheit(celsius_temperatures))