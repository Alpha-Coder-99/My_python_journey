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

# GEtter&Setter
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks  # '__' ka matlab hai ye private hai

    # GETTER: Marks dekhne ke liye
    @property
    def marks(self):
        print("Marks check kiye ja rahe hain...")
        return self.__marks

    # SETTER: Marks badalne ke liye
    @marks.setter
    def marks(self, value):
        if value < 0 or value > 100:
            print("Ghalti! Marks 0 aur 100 ke darmiyan hone chahiye.")
        else:
            print(f"Marks update ho gaye: {value}")
            self.__marks = value

# --- Testing ---
s1 = Student("Areeba", 85)

# Getter ko call karna (Bina bracket ke)
print(s1.marks) 

# Setter ko call karna
s1.marks = 95    # Sahi value: Update ho jayegi
s1.marks = 150   # Galat value: Error message aayega