class Transaction:
    def __init__(self, txn_id, from_account, to_account, amount, currency, timestamp=None):
        self.txn_id = txn_id
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount
        self.currency = currency
        self.timestamp = timestamp
        self.status = 'pending'
        self.flags = []

    def mark_flagged(self, reason):
        self.flags.append(reason)
        self.status = 'flagged'

    def mark_completed(self):
        self.status = 'completed'
