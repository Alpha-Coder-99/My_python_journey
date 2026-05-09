class Service:

    def __init__(self, name, price):

        self.name = name
        self.price = price


class Booking:

    def __init__(self):

        self.services = []


    # -------- Add Service -------- #

    def add_service(self, service):

        self.services.append(service)

        print(f"\n✅ {service.name} service booked!")


    # -------- Calculate Total -------- #

    def total_bill(self):

        return sum(service.price for service in self.services)


    # -------- Show Booking -------- #

    def show_booking(self):

        if not self.services:

            print("\n📭 No services booked yet")
            return

        print("\n====== YOUR BOOKINGS ======")

        for i, service in enumerate(self.services, 1):

            print(f"{i}. {service.name} - Rs {service.price}")

        print(f"\n💰 Total Bill: Rs {self.total_bill()}")


    # -------- Checkout -------- #

    def checkout(self):

        if not self.services:

            print("\n📭 No services selected")
            return

        self.show_booking()

        confirm = input(
            "\nConfirm booking? (yes/no): "
        ).strip().lower()

        if confirm == "yes":

            print("\n🎉 Booking Confirmed!")
            print("🏠 Our team will reach your home soon!")

            self.services.clear()

        else:

            print("\n❌ Booking canceled")


# ================= MAIN PROGRAM ================= #

def main():

    menu = [

        Service("Cleaning Service", 2000),
        Service("Electrician", 1500),
        Service("Plumber", 1800),
        Service("Painter", 3000),
        Service("AC Repair", 2500)

    ]

    booking = Booking()

    while True:

        print("\n====== HOUSE SERVICES APP ======")

        for i, service in enumerate(menu, 1):

            print(f"{i}. {service.name} - Rs {service.price}")

        print("6. View Booking")
        print("7. Checkout")
        print("8. Exit")

        choice = input("\nChoose an option: ")


        # -------- Add Service -------- #

        if choice in ["1", "2", "3", "4", "5"]:

            booking.add_service(menu[int(choice) - 1])


        # -------- View Booking -------- #

        elif choice == "6":

            booking.show_booking()


        # -------- Checkout -------- #

        elif choice == "7":

            booking.checkout()


        # -------- Exit -------- #

        elif choice == "8":

            print("\n👋 Thanks for using House Services App!")
            break


        # -------- Invalid Input -------- #

        else:

            print("\n❌ Invalid option! Please choose correctly.")


# Run App
main()