import datetime

print("🏧 --- Welcome to ATM Machine Project --- 🥰")


# ------------------ Account Data ------------------ #

password = 78912
balance = 10000
transactions = []

attempt = 0
max_attempt = 3


# ------------------ PIN Verification ------------------ #

while attempt < max_attempt:

    pin = int(input("\nEnter your 5-digit PIN: "))

    if pin == password:
        print("\n✅ Access Granted!")
        break

    else:
        attempt += 1
        remaining = max_attempt - attempt

        print(f"\n❌ Incorrect PIN! Attempts left: {remaining}")

# If all attempts finished
if attempt == max_attempt:
    print("\n🚫 Sorry! Your account is blocked.")
    

# ------------------ ATM Menu ------------------ #

else:

    while True:

        print("\n====== ATM MENU ======")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Mini Statement")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        # ---------- Check Balance ---------- #

        if choice == "1":

            print(f"\n💰 Current Balance: Rs {balance}")

        # ---------- Deposit ---------- #

        elif choice == "2":

            deposit = int(input("\nEnter amount to deposit: Rs "))

            if deposit > 0:

                balance += deposit

                time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                transactions.append(
                    (time, f"Deposited Rs {deposit}")
                )

                print(f"\n✅ Deposit Successful!")
                print(f"💰 New Balance: Rs {balance}")

            else:
                print("\n❌ Invalid amount!")

        # ---------- Withdraw ---------- #

        elif choice == "3":

            withdraw = int(input("\nEnter amount to withdraw: Rs "))

            if withdraw <= balance and withdraw > 0:

                balance -= withdraw

                time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                transactions.append(
                    (time, f"Withdraw Rs {withdraw}")
                )

                print(f"\n✅ Withdrawal Successful!")
                print(f"💰 Remaining Balance: Rs {balance}")

            elif withdraw <= 0:
                print("\n❌ Invalid amount!")

            else:
                print("\n❌ Insufficient Balance!")

        # ---------- Mini Statement ---------- #

        elif choice == "4":

            print("\n====== MINI STATEMENT ======")

            if not transactions:
                print("📄 No transactions yet.")

            else:

                for t in transactions:
                    print(f"{t[0]}  --->  {t[1]}")

                print(f"\n💰 Available Balance: Rs {balance}")

        # ---------- Exit ---------- #

        elif choice == "5":

            exit_choice = input(
                "\nAre you sure you want to exit? (yes/no): "
            )

            if exit_choice.lower() == "yes":

                print("\n🙏 Thanks for using our ATM Machine!")
                print("👋 Visit Again!")

                break

            elif exit_choice.lower() == "no":
                continue

            else:
                print("\n❌ Invalid input!")

        # ---------- Invalid Option ---------- #

        else:
            print("\n❌ INVALID INPUT! Please select 1 to 5.")