import random

def spin_row():
    symbols = ["🍉", "🍋", "🍒", "🍇", "💎"]

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print("☆☆☆☆☆☆☆☆☆☆")
    print(" | ".join(row))
    print("☆☆☆☆☆☆☆☆☆☆")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍉":
            return bet * 2
        elif row[0] == "🍋":
            return bet * 3
        elif row[0] == "🍒":
            return bet * 5
        elif row[0] == "🍇":
            return bet * 10
        elif row[0] == "💎":
            return bet * 100
    return 0

def main():
    balance = 100
    print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
    print("Welcome to my Python slots")
    print("symbols:  🍉 🍋 🍒 🍇 💎")
    print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")

    while balance > 0:
        print(f"\ncurrent balance is: {balance} CHF")
        bet = input("place your bet amount: ")

        if not bet.isdigit():
            print("please enter a valid number")
            continue

        bet = int(bet)
        if bet > balance:
            print("Insufficient funds!")
            continue

        if bet <= 0:
            print("the amount is not valid")
            continue

        balance -= bet
        row = spin_row()
        print("spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"🎉 You win {payout} CHF!")
            balance += payout
        else:
            print(f"😢 Sorry, you lost {bet} CHF.")

        play_again = input("would u like to play again(Y/N)? ").upper()
        if play_again != "Y":
            break

    print("Thanks for playing! Goodbye 👋")
if __name__ == "__main__":
    main()