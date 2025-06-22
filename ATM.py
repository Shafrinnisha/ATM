# **ATM System :**

'''
This directory contains the source code for a simple ATM system simulator written in Python

**Features:**

User accounts with unique IDs, PINs, and balances.
Deposit, withdraw, and transfer functionalities for account holders.
Transaction history tracking for each user account.

**How it works:**

* The program starts by creating an ATM object and initializing some sample user accounts.
* Users can enter their ID and PIN for authentication.
* If successful, a menu is displayed with options for deposits, withdrawals, transfers, viewing transaction history, or quitting.
* Based on the user's choice, the program interacts with their account object to perform the chosen action.

**Note:**

* This is a basic simulation program and does not connect to a real banking system. Account information is stored in memory and not persisted.
* The code prioritizes readability and functionality over security best practices. In a real-world scenario, additional security measures would be necessary.

'''

'''
**UserAccount Class:**

* This class represents a user account in the ATM system.
* **Attributes:**
    * `user_id`: Unique identifier for the user (string).
    * `pin`: User's PIN for authentication (integer).
    * `balance`: Current balance in the account (float).
    * `transaction_history`: List of strings storing transaction details (e.g., deposits, withdrawals, transfers).
* **Methods:**
    * `__init__`: Initializes a new `UserAccount` object with the provided user ID, PIN, and initial balance.
    * `deposit`: Adds the specified amount to the user's balance and updates the transaction history.
    * `withdraw`: Attempts to withdraw the specified amount from the balance. If successful, it updates the transaction history. Otherwise, it prints an "Insufficient balance!" message.
    * `transfer`: Transfers the specified amount from the user's account to another user's account (provided as an argument) and updates both users' transaction histories. Again, it checks for sufficient balance before transferring.
    * `view_transaction_history`: Prints each transaction from the user's transaction history.
'''


class UserAccount:
    def __init__(self, user_id, pin, balance):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
        else:
            print("Insufficient balance!")

    def transfer(self, recipient, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to {recipient.user_id}")
        else:
            print("Insufficient balance!")

    def view_transaction_history(self):
        for transaction in self.transaction_history:
            print(transaction)

'''
**ATM Class:**

* This class represents the ATM machine itself.
* **Attributes:**
    * `users`: Dictionary to store all user accounts (key: user ID, value: corresponding UserAccount object).
* **Methods:**
    * `__init__`: Initializes an empty `ATM` object with an empty user dictionary.
    * `create_account`: Creates a new `UserAccount` object with the provided information and adds it to the user dictionary.
    * `authenticate_user`: Checks if a user with the given ID and PIN exists. If valid, it returns the corresponding `UserAccount` object. Otherwise, it returns None.
'''


class ATM:
    def __init__(self):
        self.users = {}  # Store user accounts (user_id: UserAccount)

    def create_account(self, user_id, pin, initial_balance):
        self.users[user_id] = UserAccount(user_id, pin, initial_balance)

    def authenticate_user(self, user_id, pin):
        if user_id in self.users and self.users[user_id].pin == pin:
            return self.users[user_id]
        else:
            return None
'''
**main Function:**

* This function simulates the ATM user interaction.
* It creates an `ATM` object and initializes some user accounts with IDs, PINs, and starting balances.
* It prompts the user for their ID and PIN and tries to authenticate them using the `ATM` object's `authenticate_user` method.
* If authentication is successful, it presents a menu with options for deposit, withdrawal, transfer, viewing transaction history, and quitting.
* Based on the user's choice, it calls the appropriate methods of the user's account object (obtained during authentication).
'''

def main():
    atm = ATM()
    atm.create_account("me", 2004, 10000)
    atm.create_account("octanet", 2024, 100000)
    atm.create_account("intern", 2023, 1000)

    user_id = input("Enter your user ID: ")
    pin = int(input("Enter your PIN: "))

    user = atm.authenticate_user(user_id, pin)
    if user:
        print(f"Welcome, {user.user_id}!")
        while True:
            print("\nOptions:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer")
            print("4. View Transaction History")
            print("5. Quit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                amount = float(input("Enter deposit amount: "))
                user.deposit(amount)
            elif choice == 2:
                amount = float(input("Enter withdrawal amount: "))
                user.withdraw(amount)
            elif choice == 3:
                recipient_id = input("Enter recipient's user ID: ")
                recipient = atm.users.get(recipient_id)
                if recipient:
                    amount = float(input("Enter transfer amount: "))
                    user.transfer(recipient, amount)
                else:
                    print("Recipient not found.")
            elif choice == 4:
                user.view_transaction_history()
            elif choice == 5:
                print("Thank you for using our ATM!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
    else:
        print("Authentication failed. Invalid user ID or PIN.")
if __name__ == "__main__":
    main()


