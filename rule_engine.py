from logger import Logger
from notification import Notifier
from audit import AuditTrail

#comment
class RuleEngine:
    def __init__(self, rules, logger=None, notifier=None, audit_trail=None, rates=None):
        self.rules = rules
        self.logger = logger or Logger()
        self.notifier = notifier or Notifier()
        self.audit_trail = audit_trail or AuditTrail()
        self.rates = rates or {}

    def process(self, transaction, accounts):
        self.logger.log(f"Processing transaction {transaction.txn_id}")
        self.audit_trail.record(transaction, 'start')
        for rule in self.rules:
            if not rule.apply(transaction, accounts):
                self.logger.log(f"Transaction {transaction.txn_id} flagged: {transaction.flags[-1]}")
                self.notifier.notify_flagged(transaction)
                self.audit_trail.record(transaction, 'flagged')
                return False
        # If all rules pass
        from_acc = accounts.get(transaction.from_account)
        to_acc = accounts.get(transaction.to_account)
        if from_acc and to_acc:
            from utils import currency_convert
            # Debit sender by original amount in their currency
            if from_acc.currency != transaction.currency:
                amount_to_debit = currency_convert(transaction.amount, transaction.currency, from_acc.currency, self.rates)
            else:
                amount_to_debit = transaction.amount
            # Credit recipient by transaction amount in their currency
            if to_acc.currency != transaction.currency:
                amount_to_credit = currency_convert(transaction.amount, transaction.currency, to_acc.currency, self.rates)
            else:
                amount_to_credit = transaction.amount
            if from_acc.debit(amount_to_debit):
                to_acc.credit(amount_to_credit)
                transaction.mark_completed()
                self.logger.log(f"Transaction {transaction.txn_id} completed.")
                self.audit_trail.record(transaction, 'completed')
                return True
            else:
                transaction.mark_flagged("Insufficient funds for debit")
                self.logger.log(f"Transaction {transaction.txn_id} failed to debit sender.")
                self.audit_trail.record(transaction, 'failed')
                return False
        else:
            transaction.mark_flagged("Transfer failed")
            self.logger.log(f"Transaction {transaction.txn_id} failed to transfer.")
            self.audit_trail.record(transaction, 'failed')
            return False
