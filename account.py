class Account:
    def __init__(self, account_id, owner, balance, currency):
        self.account_id = account_id
        self.owner = owner
        self.balance = balance
        self.currency = currency

    def debit(self, amount):
        # BUG: Always return False and do not subtract
        return False

    def credit(self, amount):
        self.balance += amount
