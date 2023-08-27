list = [1, 2, 3, 2, 4, 1, 5, 2]
unique = []
two = []
for i in list:
    if i not in unique:
        unique.append(i)
    else:
        two.append(i)
print(two)
# Вопрос - как слелать так, чтобы в списке two не было повторяющихся элементов?
#У меня появляется только идея создать очередную такую проверку.


#↓ решение из интернета. Оставляю для себя как один из самых понятных вариантов.
#for point in list:
#    if list.count(point) > 1 and point not in two:
#       two.append(point)

#print("Повторяющиеся элементы :", two)