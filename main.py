import os
import random
from datetime import datetime


class BankAccount:
    # Constructor for the BankAccount class.
    def __init__(self, username, accountType, balance=0):
        # Initialize main attributes: username, account type, and balance.
        self.username = username
        self.accountType = accountType
        self.balance = balance

        # Generate a unique account ID for each new account.
        self.accountID = self.generate_accountID()

        # Prepare filename based on user's details.
        self.filename = f"{self.username}_{self.accountType}_{self.accountID}.txt"

        # Create an initial transaction file for the account.
        with open(self.filename, 'w') as file:
            file.write("Sahi International Bank\n")
            file.write(f"Account Holder: {self.username}\n")
            file.write(f"Account Type: {self.accountType}\n")
            file.write(f"Account ID: {self.accountID}\n\n")
            file.write("Transaction History:\n")
            file.write("Account created\n")

    # Utility method to generate a random account ID.
    def generate_accountID(self):
        return str(random.randint(1000, 9999))

    # Helper method to record transactions with timestamps.
    def record_transaction(self, transaction):
        with open(self.filename, 'a') as file:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            file.write(f"{timestamp} - {transaction}\n")

    # Method to handle deposit operations.
    def deposit(self, amount):
        self.balance += amount
        transaction = f"Deposited ${amount}. Balance: ${self.balance}"
        self.record_transaction(transaction)

    # Method to handle withdrawal operations, with balance checks.
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return
        self.balance -= amount
        transaction = f"Withdrew ${amount}. Balance: ${self.balance}"
        self.record_transaction(transaction)

    # Retrieve the current balance.
    def get_balance(self):
        return self.balance

    # Getter methods for account details.
    def get_userID(self):
        return self.accountID

    def get_username(self):
        return self.username

    def get_accountType(self):
        return self.accountType

    # Retrieve the transaction history from the file.
    def get_transaction_history(self):
        with open(self.filename, 'r') as file:
            return file.read()


def main():
    # Sample usage of the BankAccount class.

    # Create and operate on Arshdeep's checking account.
    account1 = BankAccount("Arshdeep", "Chequing")
    account1.deposit(568)
    account1.withdraw(209)
    account1.withdraw(53)
    print(account1.get_transaction_history())

    # Create and operate on Dhanbir's savings account.
    account2 = BankAccount("Dhanbir", "Saving")
    account2.deposit(1497)
    account2.withdraw(123)
    print(account2.get_transaction_history())

    # Create and operate on Deepasis's savings account.
    account3 = BankAccount("Deepasis", "Saving")
    account3.deposit(57)
    account3.withdraw(11)
    account3.deposit(2560)
    print(account3.get_transaction_history())


if __name__ == '__main__':
    # Execute the main function when the script is run directly.
    main()