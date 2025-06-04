def currency_convert(amount, from_currency, to_currency, rates):
    if from_currency == to_currency:
        return amount
    rate = rates.get((from_currency, to_currency), 1)
    return amount * rate
