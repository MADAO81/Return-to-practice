n = int(input("n: ")) # сколько чисел в таблице
num_line = 1
while num_line <= n:
    i = 1
    while i <= n:
        print(f"{i * num_line:>2}", end=" ")
        i +=1
    print()
    num_line +=1