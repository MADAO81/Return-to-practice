class BankAccount:

    def receive(self, amount):  # пункт б
        self.balance += amount

    def send(self, amount):  # пункт в, с return'ом
        # может быть много причин когда платёж не произойдёт
        # и только один случай когда произойдёт

        # такая конструкция, которая является условным оператором, заканчивающемся return'ом
        # назвается guard clause
        if self.balance < amount:
            raise ValueError('Недостаточно средств')  # здесь лучше сделать свой тип исключений, но пока не умеем

        if str(self.card)[0] == '4':  # если номер начинается с "4"
            raise TypeError('Visa не обслуживаются')

        # если мы здесь, значит никакой return не произошёл
        # это значит, что ни одно условие не сработало
        # это значит, что всё хорошо
        self.balance -= amount
        return 0

    def __init__(self, card_number, name, initial_balance, currency, status):
        #print('Мы в конструкторе')
        self.card = card_number  # создал атрибут
        self.name = name  # название атрибута и аргумента могут совпадать
        self.balance = initial_balance
        self.currency = currency
        self.client_status = status


# a1 = BankAccount()  # конструктор по умолчанию
# a1.card = 562835628
# a1.name = "Эльвира"
# a1.balance = 5283.5

a1 = BankAccount(562835628, "Xena", 5283.5,'EURO', "VIP")  # Конструктор

# Есть другие типы конструкторов
# например, конструктора копирования, но их питоне обычно не делают
# /!\ В отличие от некоторых других языков, в питоне конструктор у класса только один

result = a1.send(500)
print(a1.balance, result)