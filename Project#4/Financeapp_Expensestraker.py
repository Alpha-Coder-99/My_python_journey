# Expense tracker app projetct
expenses=[] #LIst of expenses in form of dictionaries
print("--- WElcome to Alpha's Expense tracker🥰😳 ---")
while True:
    print("===Menu===")
    print("1.Add expenses💸")
    print("2.View all expenses💸")
    print("3.View total expenses💸")
    print("4.exit")

    choice=int(input("please enter your choice"))

    if choice==1:
        date=input("Enter the date of expense:")
        category=input("Enter the Category of expense(food, self care, grocery,medicine,clothes,books...etc):")
        description=input("Enter a bit detail of your expense")
        amount=float(input("Enter total amount of your expenses"))
        expense={
            "date":date,
            "category": category,
            "description":description,
            "amount":amount

        }
        