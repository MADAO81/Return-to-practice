cost = float(input("Стоимость товара: "))
quantity = int(input("Количество: "))

count = 1
while count <= quantity:
    # print(count, format(cost * count, ".2f"), "рублей")
    print(f"{count} {count * cost:.2f} рублей")
    count +=1