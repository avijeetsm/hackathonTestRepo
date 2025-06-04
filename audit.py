class AuditTrail:
    def __init__(self):
        self.trail = {}

    def record(self, transaction, event):
        if transaction.txn_id not in self.trail:
            self.trail[transaction.txn_id] = []
        self.trail[transaction.txn_id].append(event)

    def get_trail(self, txn_id):
        return self.trail.get(txn_id, [])
