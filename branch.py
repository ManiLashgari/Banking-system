"""
branch.py
"""
class Branch:
    """
    Reprasent a bank branch.
    """
    def __init__(self, branch_id: str, branch_address: str,\
                  branch_accounts_list: list, employees_list: list):
        self.branch_id = branch_id
        self.branch_address = branch_address
        self.branch_accounts_list = branch_accounts_list
        self.employees_list = employees_list
        