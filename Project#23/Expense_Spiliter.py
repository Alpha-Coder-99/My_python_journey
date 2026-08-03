print("===WELCOME TO OUR EXPENSE SPLITTER===")

menu = {
    "pizza": 2000,
    "burger": 1000,
    "ice cream": 500,
    "samosa": 100,
    "coca cola": 300,
    "chana chat": 200
}

def display_menu():
    print("\n--- MENU ---")
    for item, price in menu.items():
        print(f"{item.capitalize()}: Rs. {price}")
    print("-----------------")

def calculate_expenses():
    num_people = int(input("\nHow many people are there? "))
    if num_people <= 0:
        print("At least 1 person must be present.")
        return
    
    people_orders = []

    for i in range(1, num_people + 1):
        print(f"\n--- Person {i}'s Order ---")
        display_menu()
        
        person_total = 0
        
        while True:
            choice = input("Do you want to order anything? (yes/no): ").lower().strip()
            if choice == 'no':
                break
            elif choice == 'yes':
                item_name = input("Write item name according to menu: ").lower().strip()
                
                if item_name in menu:
                    sharers = int(input(f"How many people want to share this '{item_name}'? (e.g., Type 1 if you want to eat it alone): "))
                    if sharers > 0:
                        item_price = menu[item_name]
                        share_price = item_price / sharers
                        person_total += share_price
                    else:
                        print("Number of sharers must be greater than 0.")
                else:
                    print("This item doesn't exist in the menu. Please choose a valid item.")
            else:
                print("Only enter 'yes' or 'no'.")
        
        people_orders.append(person_total)

    print("\n" + "="*30)
    print("      FINAL BILL ")
    print("="*30)

    grand_total = 0

    for i, subtotal in enumerate(people_orders, start=1):
        tax = subtotal * 0.10
        total_with_tax = subtotal + tax
        grand_total += total_with_tax
        
        print(f"Person {i}:")
        print(f"  - Subtotal : Rs. {subtotal:.2f}")
        print(f"  - 10% Tax  : Rs. {tax:.2f}")
        print(f"  - Total    : Rs. {total_with_tax:.2f}\n")

    print(f"Grand Total (Including Tax): Rs. {grand_total:.2f}")
    print("="*30)

calculate_expenses()