# Банковское приложение
y = 5
x = 50000

def bank(x, y):
    account_balance = x
    rate = 0.10
    for _ in range(y):
        account_balance += account_balance * rate
    return account_balance

balance_after_years = bank(50000, 5)
print("Спустя", y, "лет у клиента на счету будет:",balance_after_years)
