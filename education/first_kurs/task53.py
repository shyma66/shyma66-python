import json
x = '{ "name":"Liubov", "age":25, "city":"Lviv"}' # some JSON
y = json.loads(x) # parse x
print("Data from JSON: ", y)
print(type(y)) # the result is a Python dictionary
print("Age: ", y["age"])