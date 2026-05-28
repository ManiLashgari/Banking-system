from account import Account

class Customer:
    def __init__(self, name: str, customer_id: str, national_id: str, accounts_list: list = []):
        self.name = name
        self.customer_id = customer_id
        self.national_id = national_id
        self.accounts_list = accounts_list

    def add_account(self):
        self.accounts_list.append(Account(self.name).get_info())

    def get_accounts_list(self):
        return self.accounts_list
    
    def get_total_balance(self):
        ...