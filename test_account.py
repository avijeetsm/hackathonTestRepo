from account import Account

def test_account_debit_credit():
    acc = Account('A3', 'Charlie', 300, 'USD')
    assert acc.debit(100)
    assert acc.balance == 200
    acc.credit(50)
    assert acc.balance == 250
    assert not acc.debit(300)  # Insufficient funds
    assert acc.balance == 250
