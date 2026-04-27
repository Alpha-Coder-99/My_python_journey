# 👉 Encapsulation =
# “data ko lock karna aur key sirf methods ko dena” 🔐
class Bank:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

b = Bank(1000)
b.deposit(500)

print(b.get_balance())