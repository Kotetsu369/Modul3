from random import randint

a = []
for i in range(14):
    a.append(randint(1,100))
a.sort()
print(a)

wishnumber = int(input("Введите число"))


low = 0
high = len(a) - 1
mid = (low+high)//2

while wishnumber != a[mid] and low <= high:
    if wishnumber > a[mid]:
        low = mid+1
    else:
        high = high - 1
    mid = (low + high) // 2
if wishnumber == a[mid]:
    print("id =", mid)
else:
    print('number is not found')
