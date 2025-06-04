from transaction import Transaction
from account import Account

def test_transaction_basic():
    acc1 = Account('A1', 'Alice', 1000, 'USD')
    acc2 = Account('A2', 'Bob', 500, 'USD')
    txn = Transaction('T1', 'A1', 'A2', 200, 'USD')
    assert txn.status == 'pending'
    acc1.debit(200)
    acc2.credit(200)
    txn.mark_completed()
    assert acc1.balance == 800
    assert acc2.balance == 700
    assert txn.status == 'completed'
