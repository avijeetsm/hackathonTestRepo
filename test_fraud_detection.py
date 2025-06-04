from transaction import Transaction
from account import Account
from rule import FraudRule
from rule_engine import RuleEngine

def test_fraud_rule_insufficient_funds():
    acc1 = Account('A1', 'Alice', 100, 'USD')
    acc2 = Account('A2', 'Bob', 500, 'USD')
    accounts = {'A1': acc1, 'A2': acc2}
    rules = [FraudRule()]
    txn = Transaction('T3', 'A1', 'A2', 200, 'USD')
    engine = RuleEngine(rules)
    assert not engine.process(txn, accounts)
    assert txn.status == 'flagged'
    assert 'Insufficient funds' in txn.flags[0]
