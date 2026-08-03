print("===WELCOME TO OUR EXPENSE SPLITTER===")

menu={
    "pizza":"2000",
    "Burgur":"1000",
    "Ice cream":"500",
    "Samosa":"100",
    "coca cola":"300",
    "Chana chat":"200"
    
}


def display_menu():
    print("\n--- MENU ---")
    for item, price in menu.items():
        print(f"{item.capitalize()}: Rs. {price}")
    print("------------")

def calculate_expenses():
     
    num_people = int(input("\nKitne log hain total? "))
    if num_people <= 0:
        print("Atleast 1 person should be must")
        return
        

    
    people_orders = []

    for i in range(1, num_people + 1):
        print(f"\n--- Person {i} 's Order ---")
        display_menu()
        
        person_total = 0
        
        while True:
            choice = input("Kya aap menu se koi cheez order karna chahte hain? (yes/no): ").lower()
            if choice == 'no':
                break
            elif choice == 'yes':
                item_name = input("Item ka naam likhein (menu ke mutabiq): ").lower()
                
                if item_name in menu:
                    sharers = int(input(f"Yeh '{item_name}' kitne log mil kar share kar rahe hain? (e.g., 1 agar akelay khana hai): "))
                    if sharers <= 0:
                        sharers = 1

                    item_price = menu[item_name]
                    share_price = item_price / sharers
                    person_total += share_price
                else:
                    print("Yeh item menu mein mojood nahi hai. Dobara koshish karein.")
            else:
                print("Sirf 'yes' ya 'no' enter karein.")
        
        people_orders.append(person_total)

    print("\n" + "="*30)
    print("   FINAL BILL & SPLIT SUMMARY")
    print("="*30)

    grand_total = 0

    for i, subtotal in enumerate(people_orders, start=1):
        # 10% Tax calculation
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



