# Object-Oriented Programming (OOP)

This repository explores the fundamental concepts of Object-Oriented Programming (OOP) in Python through a practical Bank Account project.  It's designed to help you understand and apply OOP principles to real-world scenarios.

## What is Object-Oriented Programming?

OOP is a programming paradigm based on the concept of "objects," which can contain data (attributes) and code (methods) that operate on that data.  Key principles of OOP include:

* **Abstraction:**  Simplifying complex systems by modeling only the essential parts of an object.
* **Encapsulation:**  Bundling data and methods that operate on that data within a class, and controlling access to the data.
* **Inheritance:**  Creating new classes (derived classes) based on existing classes (base classes), inheriting their attributes and methods.
* **Polymorphism:**  The ability of objects of different classes to respond to the same method call in their own specific ways.

## Bank Account Project

This project implements a simple bank account system using OOP principles. It demonstrates how to create classes, define attributes and methods, and apply OOP concepts to a practical problem.

### Classes

* **`BankAccount`:**  Represents a bank account.

### Attributes

* `account_number` (string): The unique account number.
* `account_holder` (string): The name of the account holder.
* `balance` (float): The current balance of the account.

### Methods

* `__init__(self, account_number, account_holder)`: Constructor to initialize a new `BankAccount` object.
* `deposit(self, amount)`: Deposits the given amount into the account.
* `withdraw(self, amount)`: Withdraws the given amount from the account (with error handling for insufficient funds).
* `get_balance(self)`: Returns the current balance of the account.
* `__str__(self)`: Returns a string representation of the account (e.g., for printing).

### Example Usage

```python
from bank_account import BankAccount  # Assuming the class is in bank_account.py

account = BankAccount("1234567890", "John Doe")
print(account)  # Output: Account Number: 1234567890, Account Holder: John Doe, Balance: 0.0

account.deposit(1000)
print(account)  # Output: Account Number: 1234567890, Account Holder: John Doe, Balance: 1000.0

account.withdraw(500)
print(account)  # Output: Account Number: 1234567890, Account Holder: John Doe, Balance: 500.0

account.withdraw(700)  # This will raise an InsufficientFundsError
