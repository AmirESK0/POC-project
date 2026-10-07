def show_balance(balance):
    print(f"your balance is {balance:.2f} CHF.")

def deposit():
    print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
    deposit_money = float(input("how much money would u like to deposit? "))
    if deposit_money < 0:
        print("that is not a valid amount")
        return 0
    else:
        print(f"the {deposit_money:.2f} CHF has successfully been deposited.")
    print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
    return deposit_money

def withdraw(balance):
    print("\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
    withdraw_money = float(input("how much money would u like to withdraw? "))
    if withdraw_money < 0:
        print("That is not a valid amount.")
        return 0
    elif withdraw_money > balance:
        print("Insufficient funds!")
        return 0
    else:
        print(f"the {withdraw_money:.2f} CHF has successfully been withdrawn.")
    print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")


def main():
    balance = 0
    is_running = True

    while is_running:
        print("\nbanking program")
        print("1. show balance")
        print("2. deposit money")
        print("3. withdraw money")
        print("4. exit the program")

        choice = input("enter your choice(1-4): ")

        match choice:
            case "1":
                show_balance(balance)
            case "2":
                balance += deposit()
            case "3":
                balance -= withdraw(balance)
            case "4":
                is_running = False
            case _:
                print(f"{choice} is not a valid input")

    print("Thanks! Have a nice day!")

if __name__ == "__main__":
    main()