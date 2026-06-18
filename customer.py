"""
customer.py
"""
from account import Account

class Customer:
    """
    Represents a bank customer.
    """
    def __init__(self, name: str, customer_id: str, national_id: str, accounts_list: list):
        self.name = name
        self.customer_id = customer_id
        self.national_id = national_id
        if accounts_list is None:
            accounts_list = []
        self.accounts_list = accounts_list

    def add_account(self) -> None:
        """
        Creat an account.
        """
        self.accounts_list.append(Account(self.name))

    def get_accounts_list(self) -> list:
        """
        Displaying the list of accounts.
        """
        return self.accounts_list

    def get_total_balance(self) -> str:
        """
        Displaying the balance of accounts.
        """
        total = 0
        for account in self.accounts_list:
            total += int(account.balance)
        return str(total)
