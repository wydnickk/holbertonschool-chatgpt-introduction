#!/usr/bin/python3

class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        print("Current Balance: ${:.2f}".format(self.balance))


def prompt_amount(message):
    """
    Function description:
        Prompt the user for a dollar amount and keep asking until a valid number
        is entered.

    Parameters:
        message (str): The prompt message shown to the user.

    Returns:
        float: A valid non-negative amount entered by the user.
    """
    while True:
        raw = input(message)
        try:
            amount = float(raw)
        except ValueError:
            print("Invalid amount. Please enter a numeric value (example: 10 or 10.50).")
            continue

        if amount < 0:
            print("Invalid amount. Please enter a non-negative value.")
            continue

        return amount


def main():
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ").strip().lower()

        if action == 'exit':
            break
        elif action == 'deposit':
            amount = prompt_amount("Enter the amount to deposit: $")
            cb.deposit(amount)
        elif action == 'withdraw':
            amount = prompt_amount("Enter the amount to withdraw: $")
            cb.withdraw(amount)
        elif action == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
