#Вася записал на клочке бумаги время важной встречи, но забыл, на каком именно.
#Вечером он нашел бумажку с записью пары чисел. Могут ли эти числа быть временем встречи?
#Точно известно, что оба числа целые и неотрицательные.

hours = int(input("Enter the hours: "))
minutes = int(input("Enter the minutes: "))

if hours < 24 and minutes < 60:
    print("Yes, it can be the time of meeting.")
else:
    print("No it is not the time of meeting.")