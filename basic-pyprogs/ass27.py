class BankAccount:
    def __init__(self, initial_balance=0, min_balance=1000):
        self.balance = initial_balance
        self.min_balance = min_balance

    def credit_amount(self, amount):
        self.balance += amount
        print(f"Amount {amount} credited. New balance: {self.balance}")

    def debit_amount(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
            print(f"Amount {amount} debited. New balance: {self.balance}")
        else:
            print(f"Insufficient funds! Withdrawal of {amount} not allowed.")

    def show_balance(self):
        print(f"Current balance: {self.balance}")


# Create a bank account with an initial balance of 5000 and a minimum balance of 1000
account = BankAccount(initial_balance=5000, min_balance=1000)

while True:
    print("\nMenu:")
    print("a. Credit Amount")
    print("b. Debit Amount")
    print("c. Show Balance")
    print("q. Quit")

    choice = input("Enter your choice: ")

    if choice == 'a':
        # Credit Amount
        amount = float(input("Enter the amount to credit: "))
        account.credit_amount(amount)
    elif choice == 'b':
        # Debit Amount
        amount = float(input("Enter the amount to debit: "))
        account.debit_amount(amount)
    elif choice == 'c':
        # Show Balance
        account.show_balance()
    elif choice == 'q':
        # Quit the program
        break
    else:
        print("Invalid choice. Please enter a, b, c, or q.")
