"""
bank.py
"""
from customer import Customer
from branch import Branch

class Bank:
    """
    Represents a bank.
    """
    def __init__(self, name: str, branches_list=None):
        self.name = name

        if branches_list is None:
            self.branches_list = []
        else:
            self.branches_list = branches_list

    def add_branch(self, branch: Branch) -> None:
        """
        Add a new branch to the branchs list.
        """
        self.branches_list.append(branch)

    def get_branches(self) -> list:
        """
        Return branches list.
        """
        return self.branches_list

    def find_account(self, account_id : str) -> Customer:
        """
        Return an account.
        """
        return Customer.get_accounts_list(account_id)
