def God():
    Adam = Man()
    Eve = Woman()

    return [Adam,Eve]
class Human:
    pass
class Man(Human):
    pass
class Woman(Human):
    pass

paradise = God()
print(isinstance(paradise[0], Man) , True, "First object are a man")