def words5(S):
    w5 = []
    for word in S.split():
        if len(word) < 5:
            w5.append(word)
    return w5

S = input("Введите текст")
print(words5(S))
