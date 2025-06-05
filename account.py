class Account:
    def __init__(self, account_id, owner, balance, currency):
        self.account_id = account_id
        self.owner = owner
        self.balance = balance
        self.currency = currency

    def debit(self, amount):
        return False
        # if amount > self.balance:
        #     return False
        # self.balance -= amount
        # return True

    def credit(self, amount):
        self.balance += amount
