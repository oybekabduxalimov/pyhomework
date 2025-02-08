

import json
import os
from threading import Lock

class Account:
    def __init__(self, account_number: int, name: str, balance: float):
        if not isinstance(account_number, int) or account_number <= 0:
            raise ValueError("Account number must be a positive integer.")
        if not isinstance(name, str) or not name.strip() or not name.replace(" ", "").isalpha():
            raise ValueError("Name must be a non-empty string containing only alphabetic characters and spaces.")
        if not isinstance(balance, (int, float)) or balance < 0:
            raise ValueError("Balance must be a non-negative number.")

        self.account_number = account_number
        self.name = name.strip()
        self.balance = round(float(balance), 2)

    def deposit(self, amount: float):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self.balance += round(amount, 2)
        return f"Successfully deposited ${amount:.2f}. New balance: ${self.balance:.2f}"

    def withdraw(self, amount: float):
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
        self.balance -= round(amount, 2)
        return f"Successfully withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"

    def to_dict(self):
        return {"account_number": self.account_number, "name": self.name, "balance": self.balance}

    @staticmethod
    def from_dict(data):
        return Account(data["account_number"], data["name"], data["balance"])

    def __str__(self):
        return f"Account No: {self.account_number}, Name: {self.name}, Balance: ${self.balance:.2f}"


class FileHandler:
    def __init__(self, file_name):
        self.file_name = file_name
        self.lock = Lock()

    def save(self, data):
        with self.lock:
            with open(self.file_name, "w") as file:
                json.dump(data, file, indent=4)

    def load(self):
        with self.lock:
            if os.path.exists(self.file_name):
                with open(self.file_name, "r") as file:
                    return json.load(file)
            return {}


class Bank:
    FILE_NAME = "accounts.json"

    def __init__(self):
        self.file_handler = FileHandler(self.FILE_NAME)
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name: str, initial_deposit: float):
        account_number = self._generate_account_number()
        account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        self.save_to_file()
        return f"Account created successfully! Account Number: {account_number}"

    def view_account(self, account_number: int):
        account = self._get_account(account_number)
        return str(account)

    def deposit(self, account_number: int, amount: float):
        account = self._get_account(account_number)
        result = account.deposit(amount)
        self.save_to_file()
        return result

    def withdraw(self, account_number: int, amount: float):
        account = self._get_account(account_number)
        result = account.withdraw(amount)
        self.save_to_file()
        return result

    def delete_account(self, account_number: int):
        account = self._get_account(account_number)
        del self.accounts[account_number]
        self.save_to_file()
        return f"Account {account_number} ({account.name}) has been successfully deleted."

    def transfer(self, from_account: int, to_account: int, amount: float):
        sender = self._get_account(from_account)
        receiver = self._get_account(to_account)
        sender.withdraw(amount)
        receiver.deposit(amount)
        self.save_to_file()
        return f"Successfully transferred ${amount:.2f} from Account {from_account} to Account {to_account}."

    def list_accounts(self):
        if not self.accounts:
            return "No accounts available."
        return "\n".join(str(account) for account in self.accounts.values())

    def save_to_file(self):
        data = {acc_no: acc.to_dict() for acc_no, acc in self.accounts.items()}
        self.file_handler.save(data)

    def load_from_file(self):
        data = self.file_handler.load()
        self.accounts = {int(acc_no): Account.from_dict(acc) for acc_no, acc in data.items()}

    def _generate_account_number(self):
        return max(self.accounts.keys(), default=1000) + 1

    def _get_account(self, account_number: int):
        account = self.accounts.get(account_number)
        if not account:
            raise ValueError("Account not found.")
        return account


if __name__ == "__main__":
    bank = Bank()

    while True:
        print("\nWelcome to the Bank System!")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Delete Account")
        print("6. Transfer Money")
        print("7. List All Accounts")
        print("8. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                name = input("Enter your name: ").strip()
                initial_deposit = float(input("Enter initial deposit amount: "))
                print(bank.create_account(name, initial_deposit))

            elif choice == "2":
                acc_num = int(input("Enter your account number: "))
                print(bank.view_account(acc_num))

            elif choice == "3":
                acc_num = int(input("Enter your account number: "))
                amount = float(input("Enter deposit amount: "))
                print(bank.deposit(acc_num, amount))

            elif choice == "4":
                acc_num = int(input("Enter your account number: "))
                amount = float(input("Enter withdrawal amount: "))
                print(bank.withdraw(acc_num, amount))

            elif choice == "5":
                acc_num = int(input("Enter your account number: "))
                print(bank.delete_account(acc_num))

            elif choice == "6":
                from_acc = int(input("Enter sender's account number: "))
                to_acc = int(input("Enter receiver's account number: "))
                amount = float(input("Enter transfer amount: "))
                print(bank.transfer(from_acc, to_acc, amount))

            elif choice == "7":
                print(bank.list_accounts())

            elif choice == "8":
                bank.save_to_file()
                print("Thank you for using the bank system. Your accounts are safely saved. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

        except ValueError as e:
            print(f"Error: {e}")
