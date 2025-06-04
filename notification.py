class Notifier:
    def __init__(self):
        self.notifications = []

    def notify_flagged(self, transaction):
        msg = f"Transaction {transaction.txn_id} flagged: {transaction.flags[-1]}"
        self.notifications.append(msg)
        print(msg)

    def get_notifications(self):
        return self.notifications
