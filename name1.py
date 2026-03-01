n = int(input("Введите число n: "))

sum = 0
chetnie = 0

for i in range(1, n + 1):
    sum += i

    if i % 2 == 0:
       chetnie += 1
print(sum, chetnie)