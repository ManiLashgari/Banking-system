class Bank:
    def __init__(self, name, customers_list, total_balance, branches_list):
        self.name = name
        self.customers_list = customers_list
        self.total_balance = total_balance
        self.branches_list = branches_list

    def add_branches(self, branch_name):
        ...

    def find_account(self, account_id: str):
        ...
