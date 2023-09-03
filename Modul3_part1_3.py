k = input("введите целое число")
k1 = list(str(k))
count = sum(map(int, k1))
print("Сумма цифр", count)