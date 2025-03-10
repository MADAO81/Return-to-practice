a1 = {
    'card': 5484226324895551,
    'name': 'Эльвира Горшкова',
    'currency': 'RUB',
    'balance': 3567345.0,
    'status': 'Platinum'
}

a1['balance'] += 100


def transfer(account, amount):
    account['balance'] += amount


transfer(a1, 100)






