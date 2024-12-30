import os
import random


class BankAccount:
    def __init__(self, name, accountType, balance=0):
        self.name = name
        self.accountType = accountType
        self.balance = balance
        self.accountNumber = random.randint(100000, 999999)
        self.filename = f"{self.accountNumber}_{
            self.accountType}_{self.name}.txt"
        # Create a file for the account's transaction history
        with open(self.filename, 'w') as f:
            f.write(f"Account created: {self.name}, {
                    self.accountType}, ID: {self.accountNumber}\n")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        with open(self.filename, 'a') as f:
            f.write(f"Deposited: ${amount:.2f}, New Balance: ${
                    self.balance:.2f}\n")
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        with open(self.filename, 'a') as f:
            f.write(f"Withdrew: ${amount:.2f}, New Balance: ${
                    self.balance:.2f}\n")
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def get_balance(self):
        return self.balance

    def get_account_number(self):
        return self.accountNumber

    def get_name(self):
        return self.name

    def get_account_type(self):
        return self.accountType

    def get_transaction_history(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return f.read()
        else:
            return "No transaction history found."

# Testing the BankAccount class


def main():
    print("Welcome to the Bank Account Management System!\n")

    # Create multiple bank account objects
    account1 = BankAccount("Alice", "Savings", 1000)
    account2 = BankAccount("Bob", "Chequing")

    # Perform transactions
    account1.deposit(500)
    account1.withdraw(200)
    account2.deposit(1000)
    account2.withdraw(1200)

    # Display account details
    print(f"Account 1 - Name: {account1.get_name()}, Account Type: {
          account1.get_account_type()}, Balance: ${account1.get_balance():.2f}")
    print(f"Account 2 - Name: {account2.get_name()}, Account Type: {
          account2.get_account_type()}, Balance: ${account2.get_balance():.2f}\n")

    # Display transaction history
    print("Transaction History for Account 1:")
    print(account1.get_transaction_history())

    print("Transaction History for Account 2:")
    print(account2.get_transaction_history())


if __name__ == "__main__":
    main()