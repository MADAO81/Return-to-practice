class BankAccount:  # класс, тип данных
    card = 0  # attribute, member, атрибут, свойство. Это любая переменная внутри класса.
    name = ''
    currency = ''
    balance = 0.0
    status = ''

    # функция внутри класса - метод класса method
    def receive(self, amount):  # пополнить баланс
        self.balance += amount * 0.99  # забрали 1% комиссии

    # def send(self, amount):
    #     # если требуется несгораемый остаток на счете, условие будет другое
    #     if  self.balance >= amount:
    #         self.balance -= amount

    # # Вариант с return
    # def send(self, amount):
    #     # если требуется несгораемый остаток на счете, условие будет другое
    #     if self.balance >= amount:
    #         self.balance -= amount
    #         return 0  # 0 означает что все ОК
    #     print("Недостаточно средств.")
    #     return -1  # означает что недостаточно средств


    def send(self, amount):
        # может быть много причин, когда платеж не произойдет и только один случай, когда произойдет

        # такая конструкция, которая является условным оператором, заканчивающимся return называется
        # guard clause(охранная оговорка, условие)
        if self.balance < amount:
            return  -1 # недостаточно средств

        if str(self.card)[0] == "4": # если номер начинается с 4
            return -2 # не принимаем платежи на карты, начинающиеся с 4(VISA)


        # если мы здесь, значит return не произошел
        # это значит, что ни одно из условий не сработало, значит все ОК
        self.balance -= amount
        return 0

# переменная типа BankAccount. она же экземпляр класса или объект этого класса,
# переменная этого типа, instance
a1 = BankAccount()
a2 = BankAccount()

a1.card = 1235654797
a1.name = "Xena"
a1.currency = "RUB"
a1.balance = 20000.00
a1.status = "Super Platinum"

a2.card = 7778985642
a2.name = "Hercules"
a2.currency = "EUR"
a2.balance = 1000000.00
a2.status = "Gold"

a2.receive(100)  # 1 аргумент, но на самом деле 5

print(a2.balance)

# a1.send(500)
result = a1.send(500)
print(a1.balance, result)

# a1.send(100000)
result = a1.send(100000)
print(a1.balance, result)
