"""
account.py
"""
from datetime import date


class Account:
    """
    Represents a bank account.
    """
    next_id = "1"

    def __init__(self, owner: str, balance="0", is_active=True):
        self.account_id = Account.next_id
        Account.next_id = int(Account.next_id) + 1
        self.balance = balance
        self.date = date.today()
        self.is_active = is_active
        self.owner = owner

    def deposit(self, amount: str) -> str:
        """
        Deposit money from account.
        """
        if self.is_active:
            self.balance = int(self.balance) + int(amount)
            return f"Transaction is done successfully.\nCurrent balance: {self.balance}"
        else:
            return "Your account is inactive!"

    def withdraw(self, amount: str) -> str:
        """
        Withdraw money from account.
        """
        if self.is_active:
            if float(amount) <= float(self.balance):
                self.balance = int(self.balance) - int(amount)
                return f"Transaction is done successfully.\nCurrent balance: {self.balance}"
            else:
                return "ERROR! Not enough balance"
        else:
            return "Your account is inactive!"

    def get_balance(self) -> str:
        """
        Displaying the balance of accounts.
        """
        return f"Current balance: {self.balance}"

    def get_info(self):
        """
        Displaying the information of account.
        """
        if self.is_active:
            active = "ACTIVE"
        else:
            active = "INACTIVE"
        return f"Account's information\nAccount owner: {self.owner}\nAccount ID: {self.account_id}\
            \nCurrent balance: {self.balance}\nDate: {self.date}\nThe account is {active}"

    def activation(self, active_mode: bool) -> str:
        """
        Displaying the activation of account.
        """
        self.is_active = active_mode
        if active_mode:
            active = "activated"
        else:
            active = "deactivated"
        return f"Your account has been successfully {active}"
    