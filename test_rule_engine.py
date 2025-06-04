from transaction import Transaction
from account import Account
from rule import LimitRule, BlacklistRule
from rule_engine import RuleEngine

def test_rule_engine_limit_blacklist():
    acc1 = Account('A1', 'Alice', 1000, 'USD')
    acc2 = Account('A2', 'Bob', 500, 'USD')
    accounts = {'A1': acc1, 'A2': acc2}
    rules = [LimitRule(500), BlacklistRule(['A2'])]
    txn = Transaction('T2', 'A1', 'A2', 600, 'USD')
    engine = RuleEngine(rules)
    assert not engine.process(txn, accounts)
    assert txn.status == 'flagged'
    assert 'Exceeded limit' in txn.flags[0] or 'Account blacklisted' in txn.flags[0]
