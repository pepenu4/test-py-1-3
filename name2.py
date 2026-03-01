words = input("введите слово ")

glas = "ауоыиэяюёе"
a = 0

for i in words:
    if i in glas:
       a += 1

print(a)