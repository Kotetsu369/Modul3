
list = [11, 12,8, 89]
#numbers = input('Введите числа')
#list.append(numbers)
#a = str(list)
list = sorted(list, key=lambda x: str(x)[0], reverse = True)
s = str(list)
list1 = s.replace(",", "")
s1 = ''.join(list1.split())
print(s1)