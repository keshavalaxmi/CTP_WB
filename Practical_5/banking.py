from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class BankAccount(ABC):
    account_number: int
    holder_name: str
    balance: float = 0.0

    @abstractmethod
    def deposit(self, amount: float) -> None:
        pass

    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass

    def display_balance(self) -> None:
        print("Account Number:", self.account_number)
        print("Holder Name:", self.holder_name)
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            print("Invalid deposit amount")
            return

        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)


# Create account
account = SavingsAccount(
    account_number=1001,
    holder_name="Sahithi",
    balance=5000.0
)

account.display_balance()

account.deposit(2000.0)
account.withdraw(1500.0)

print("\nFinal Account Details:")
account.display_balance()
