# This class represents a bank account with basic operations like deposit, withdraw, and displaying balance.

class BankAccount:
    def __init__(self, account_number, balance):
        """
        Initialize the bank account with account number and balance.
        """
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """
        Deposit a specified amount into the bank account.
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the bank account if sufficient funds are available.
        """
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def display_balance(self):
        """
        Display the current balance of the bank account.
        """
        print(f"Balance: {self.balance}")

# Example usage of the BankAccount class
my_account = BankAccount("123456789", 1000)
my_account.deposit(500)      # Deposit 500 into the account
my_account.withdraw(200)     # Withdraw 200 from the account
my_account.display_balance() # Display the current balance
