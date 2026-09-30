# Exercise 5: Banking Management System

## Objective

Develop a Banking Management System demonstrating inheritance and abstraction with full type hints.

## Concepts Used

### Abstraction

The `BankAccount` class is an abstract base class derived from `ABC`.

The `deposit()` and `withdraw()` methods are declared as abstract methods using `@abstractmethod`.

### Inheritance

The `SavingsAccount` class inherits from the `BankAccount` class and provides implementations for the abstract `deposit()` and `withdraw()` methods.

### Dataclass

The `@dataclass` decorator is used to automatically generate the constructor for `BankAccount`.

### Type Hints

Type hints are used for:

- Account number
- Holder name
- Balance
- Deposit amount
- Withdrawal amount
- Method return types

## Algorithm

1. Create an abstract `BankAccount` class.
2. Define account number, holder name, and balance as attributes.
3. Declare `deposit()` and `withdraw()` as abstract methods.
4. Define a method to display account details.
5. Create a `SavingsAccount` class that inherits from `BankAccount`.
6. Implement the `deposit()` method.
7. Implement the `withdraw()` method with balance validation.
8. Create a savings account object.
9. Display the initial account details.
10. Perform deposit and withdrawal operations.
11. Display the final account details.

## Input

Account Number: 1001

Holder Name: Sahithi

Initial Balance: 5000.0

Deposit Amount: 2000.0

Withdrawal Amount: 1500.0

## Output

```text
Account Number: 1001
Holder Name: Sahithi
Balance: 5000.0
Deposited: 2000.0
Withdrawn: 1500.0

Final Account Details:
Account Number: 1001
Holder Name: Sahithi
Balance: 5500.0
