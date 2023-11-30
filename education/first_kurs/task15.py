def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)


print("If Johny: ",greet(name="Johnny"))
print("Another name:", greet(name="Max"))


