from datetime import date

class Account:
    next_id = "1"

    def __init__(self, owner: str, balance="0", is_active=True):
        self.account_id = Account.next_id
        Account.next_id = int(Account.next_id) + 1
        self.balance = balance
        self.date = date.today()
        self.is_active = is_active
        self.owner = owner


# changes -> staged changes -> commit