from transaction import Transaction
from account import Account
from rule import LimitRule
from rule_engine import RuleEngine
from audit import AuditTrail

def test_audit_trail_events():
    acc1 = Account('A1', 'Alice', 1000, 'USD')
    acc2 = Account('A2', 'Bob', 500, 'USD')
    accounts = {'A1': acc1, 'A2': acc2}
    rules = [LimitRule(500)]
    audit = AuditTrail()
    engine = RuleEngine(rules, audit_trail=audit)
    txn = Transaction('T4', 'A1', 'A2', 400, 'USD')
    engine.process(txn, accounts)
    trail = audit.get_trail('T4')
    assert 'start' in trail
    assert 'completed' in trail or 'flagged' in trail or 'failed' in trail
