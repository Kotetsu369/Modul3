x = input("размер вклада")
x1 = int(x)
p = input("Размер процента (15% = 0.15)")
p1 = float (p)
y = input("Необходимая сумма")
y1 = int (y)
t = 1 # количество лет
while x1 <= y1:
    x1 = x1+x1*p1
    t += 1
else:
    print("Срок (лет)",t)
