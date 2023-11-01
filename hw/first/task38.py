class Employee:
    count = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.count +=1
    @classmethod
    def total_number_of_employees(cls):
        # Total people
        return (f"Total people: {cls.count}")

    def displays_information(self):
        # Name and Salary
        return ( f"Name: {self.name}, salary: {self.salary}$")


first_person = Employee("Andrea", 2000)
second_person = Employee("Wladut", 3500)
third_person = Employee("Fawad", 3200)
# Name and Salary
print(first_person.displays_information())
print(second_person.displays_information())
print(third_person.displays_information())
#Total people
print(Employee.total_number_of_employees())

#

print(Employee.__bases__)  # Base classes
print(Employee.__dict__)  # Class namespace
print(Employee.__name__)  # Class name
print(Employee.__module__)  # Module name
print(Employee.__doc__)  # Docstring