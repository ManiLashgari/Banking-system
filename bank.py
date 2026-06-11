class Bank:
    """
    Represents a bank.
    """
    def __init__(self, name, customers_list, total_balance, branches_list=None):
        self.name = name
        self.customers_list = customers_list
        self.total_balance = total_balance
        if branches_list is None:
            self.branches_list = []
        else:
            self.branches_list = branches_list
