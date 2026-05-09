class Coffee:

    def __init__(self, name, price):

        self.name = name
        self.price = price


class Order:

    def __init__(self):

        self.items = []


    # -------- Add Coffee -------- #

    def add_item(self, coffee):

        self.items.append(coffee)

        print(f"\n✅ Added {coffee.name} to your order")


    # -------- Calculate Total -------- #

    def total(self):

        return sum(item.price for item in self.items)


    # -------- Show Order -------- #

    def show_order(self):

        if not self.items:

            print("\n🛒 No items in your order")
            return

        print("\n====== YOUR ORDER ======")

        for i, item in enumerate(self.items, 1):

            print(f"{i}. {item.name} - $ {item.price}")

        print(f"\n💰 Total: $ {self.total():.2f}")


    # -------- Checkout -------- #

    def checkout(self):

        if not self.items:

            print("\n🛒 Your cart is empty")
            return

        self.show_order()

        confirm = input(
            "\nProceed to checkout? (yes/no): "
        ).strip().lower()

        if confirm == "yes":

            print("\n🎉 Order Confirmed!")
            print("☕ Thank you for visiting our coffee shop!")

            self.items.clear()

        else:

            print("\n❌ Checkout canceled")


# ================= MAIN PROGRAM ================= #

def main():

    menu = [

        Coffee("Espresso", 2.5),
        Coffee("Latte", 3.5),
        Coffee("Cappuccino", 3.0),
        Coffee("Americano", 2.0)

    ]

    order = Order()

    while True:

        print("\n====== COFFEE MENU ======")

        for i, coffee in enumerate(menu, 1):

            print(f"{i}. {coffee.name} - $ {coffee.price}")

        print("5. View Order")
        print("6. Checkout")
        print("7. Exit")

        choice = input("\nChoose an option: ")


        # -------- Add Coffee -------- #

        if choice in ["1", "2", "3", "4"]:

            order.add_item(menu[int(choice) - 1])


        # -------- View Order -------- #

        elif choice == "5":

            order.show_order()


        # -------- Checkout -------- #

        elif choice == "6":

            order.checkout()


        # -------- Exit -------- #

        elif choice == "7":

            print("\n👋 Thanks for visiting!")
            break


        # -------- Invalid Input -------- #

        else:

            print("\n❌ Invalid option!")


# Run program
main()
    
    
