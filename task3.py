class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            print("Insufficient balance.")
            
    def display_balance(self):
        print(f"Account Balance: {self.balance}")

account_number = input("Enter account number: ")
owner = input("Enter account owner's name: ")
account = BankAccount(account_number, owner)

while True:
    print("\nChoose an action:")
    print("1. Deposit money")
    print("2. Withdraw money")
    print("3. Display balance")

    choice = input("Enter your choice: ")

    if choice == "1":
        deposit_amount = float(input("Enter deposit amount: "))
        account.deposit(deposit_amount)
    elif choice == "2":
        withdraw_amount = float(input("Enter withdrawal amount: "))
        account.withdraw(withdraw_amount)
    elif choice == "3":
        account.display_balance()
    else:
        print("Invalid choice. Please try again.")
