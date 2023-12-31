class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.__account_number = str(account_number)
        self.__account_holder = str(account_holder)
        self.__balance = float(balance)


    def check_balance(self):
        return self.__balance
    def deposit(self,amount):
        self.__balance += amount
    def withdraw(self,amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    @property
    def account_holder(self):
        return self.__account_holder


my_account = BankAccount("123456789", "John Doe", 1000.0)
print(my_account.account_holder)

try:
    _ = my_account.account_number
    print("Should have raised AttributeError")
except AttributeError:
    print("AttributeError raised as expected")

try:
    _ = my_account.balance
    print("Should have raised AttributeError")
except AttributeError:
    print("AttributeError raised as expected")

print(my_account.check_balance())

my_account.deposit(500.0)
print(my_account.check_balance())

my_account.withdraw(250.0)
print(my_account.check_balance())

try:
    my_account.account_holder = "Jane Doe"
    print("Should have raised AttributeError")
except AttributeError:
    print("AttributeError raised as expected")

my_account.withdraw(5000.0)