list = [7, 16, 64, 65]
#a = str(list)
list = sorted(list, key=lambda x: str(x)[0], reverse = True)
s = str(list)
list1 = s.replace(",", "")
s1 = ''.join(list1.split())
print(s1)