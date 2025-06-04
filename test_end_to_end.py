from transaction import Transaction
from account import Account
from rule import LimitRule, BlacklistRule, FraudRule
from rule_engine import RuleEngine
from logger import Logger
from notification import Notifier
from audit import AuditTrail
from utils import currency_convert

def test_end_to_end_workflow():
    acc1 = Account('A1', 'Alice', 1000, 'USD')
    acc2 = Account('A2', 'Bob', 500, 'EUR')
    accounts = {'A1': acc1, 'A2': acc2}
    rules = [LimitRule(2000), BlacklistRule([]), FraudRule()]
    logger = Logger()
    notifier = Notifier()
    audit = AuditTrail()
    rates = {('USD', 'EUR'): 0.9, ('EUR', 'USD'): 1.1}
    engine = RuleEngine(rules, logger, notifier, audit, rates)
    txn = Transaction('T5', 'A1', 'A2', 100, 'USD')
    assert engine.process(txn, accounts)
    assert txn.status == 'completed'
    assert acc1.balance == 900
    # Bob should get 90 EUR (converted from 100 USD)
    assert abs(acc2.balance - (500 + currency_convert(100, 'USD', 'EUR', rates))) < 1e-6
    assert 'completed' in audit.get_trail('T5')
    assert len(notifier.get_notifications()) == 0
