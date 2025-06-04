from abc import ABC, abstractmethod

class Rule(ABC):
    @abstractmethod
    def apply(self, transaction, accounts):
        pass

class LimitRule(Rule):
    def __init__(self, limit):
        self.limit = limit

    def apply(self, transaction, accounts):
        if transaction.amount > self.limit:
            transaction.mark_flagged(f"Exceeded limit: {self.limit}")
            return False
        return True

class BlacklistRule(Rule):
    def __init__(self, blacklist):
        self.blacklist = set(blacklist)

    def apply(self, transaction, accounts):
        if transaction.from_account in self.blacklist or transaction.to_account in self.blacklist:
            transaction.mark_flagged("Account blacklisted")
            return False
        return True

class FraudRule(Rule):
    def apply(self, transaction, accounts):
        # Example: flag if from_account has insufficient funds
        from_acc = accounts.get(transaction.from_account)
        if from_acc and from_acc.balance < transaction.amount:
            transaction.mark_flagged("Insufficient funds - possible fraud")
            return False
        return True
