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

    def withdraw(self, amount: str):
        if self.is_active:
            if float(amount) <= float(self.balance):
                self.balance = int(self.balance) - int(amount)
                return f"Transaction is done successfully.\nCurrent balance: {self.balance}"
            else:
                return "ERROR! Not enough balance"
        else:
            return "Your account is inactive!"
    
    def get_balance(self):
        return f"Current balance: {self.balance}"
    
    def get_info(self):
        if self.is_active:
            active = "ACTIVE"
        else:
            active = "INACTIVE"
        return f"Account's information\nAccount owner: {self.owner}\nAccount ID: {self.account_id}\n\
                Current balance: {self.balance}\nDate: {self.date}\nThe account is {active}"