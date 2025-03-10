class BankAccount:  # класс, тип данных
    card = 0  # attribute, member, атрибут, свойство. Это любая переменная внутри класса.
    name = ''
    currency = ''
    balance = 0.0
    status = ''


# переменная типа BankAccount. она же экземпляр класса или объект этого класса,
# переменная этого типа, instance
a1 = BankAccount()
a2 = BankAccount()


a1.card = 1235654797
a1.name = "Xena"
a1.currency = "RUB"
a1.balance = 25659870.00
a1.status = "Super Platinum"

a2.card = 7778985642
a2.name = "Hercules"
a2.currency = "EUR"
a2.balance = 1000000.00
a2.status = "Gold"