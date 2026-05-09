class Food:

    def __init__(self, name, price):

        self.name = name
        self.price = price


class RestaurantOrder:

    def __init__(self):

        self.items = []


    # -------- Add Food -------- #

    def add_food(self, food):

        self.items.append(food)

        print(f"\n😋 {food.name} added to your order!")


    # -------- Total Bill -------- #

    def total_bill(self):

        return sum(item.price for item in self.items)


    # -------- Show Order -------- #

    def show_order(self):

        if not self.items:

            print("\n🍽️ Your order is empty")
            return

        print("\n====== YOUR FOOD ORDER ======")

        for i, item in enumerate(self.items, 1):

            print(f"{i}. {item.name} - Rs {item.price}")

        print(f"\n💰 Total Bill: Rs {self.total_bill()}")


    # -------- Checkout -------- #

    def checkout(self):

        if not self.items:

            print("\n🍽️ No food selected")
            return

        self.show_order()

        confirm = input(
            "\nConfirm your order? (yes/no): "
        ).strip().lower()

        if confirm == "yes":

            print("\n🎉 Order Confirmed!")
            print("🍕 Your delicious food is being prepared 😋")

            self.items.clear()

        else:

            print("\n❌ Order canceled")


# ================= MAIN PROGRAM ================= #

def main():

    menu = [

        Food("🍕 Cheese Pizza", 1200),
        Food("🍔 Zinger Burger", 650),
        Food("🍟 French Fries", 350),
        Food("🌯 Shawarma", 400),
        Food("🍗 Crispy Broast", 900),
        Food("🍝 Pasta Alfredo", 1100),
        Food("🥤 Cold Drink", 150),
        Food("🍰 Chocolate Cake", 500)

    ]

    order = RestaurantOrder()

    while True:

        print("\n====== 😋 RESTAURANT MENU 😋 ======")

        for i, food in enumerate(menu, 1):

            print(f"{i}. {food.name} - Rs {food.price}")

        print("9. View Order")
        print("10. Checkout")
        print("11. Exit")

        choice = input("\nChoose an option: ")


        # -------- Add Food -------- #

        if choice in [str(i) for i in range(1, 9)]:

            order.add_food(menu[int(choice) - 1])


        # -------- View Order -------- #

        elif choice == "9":

            order.show_order()


        # -------- Checkout -------- #

        elif choice == "10":

            order.checkout()


        # -------- Exit -------- #

        elif choice == "11":

            print("\n👋 Thanks for visiting our restaurant!")
            print("😋 Visit Again For More Delicious Food!")

            break


        # -------- Invalid Input -------- #

        else:

            print("\n❌ Invalid option! Please try again.")


# Run App
main()