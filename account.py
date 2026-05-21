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

    def deposit(self, amount: str):
        if self.is_active:
            self.balance = int(self.balance) + int(amount)
            return f"Transaction is done successfully.\nCurrent balance: {self.balance}"
        else:
            return "Your account is inactive!"