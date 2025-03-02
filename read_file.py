f = open("info.txt", "r", encoding="utf8")

for line in f:
    print(line.rstrip())

f.close()