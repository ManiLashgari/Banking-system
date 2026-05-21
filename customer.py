class Customer:
    def __init__(self, name, customer_id, national_id, accounts_list):
        self.name = name
        self.customer_id = customer_id
        self.national_id = national_id
        self.accounts_list = accounts_list

    def add_account(self, owner):
        ...

    def get_total_balance(self):
        ...