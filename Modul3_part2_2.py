from random import randint

n = 5
m = [[randint(0,100) for i in range (n)] for j in range(n)]
print (m)
b = 0
for c1 in range(n):
    for c2 in range(n):
        i = m[c1][c2]
        if i > b:
           b = i
print(b)

