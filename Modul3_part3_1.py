import math


def area(a, b, c):
    P = ((a + b + c) / 2)
    P1 = P * (P - a) * (P - b) * (P - c)
    S = math.sqrt(P1)
    return (S)


a = int(input("input a"))
b = int(input("input b"))
c = int(input("input c"))
print(area(a, b, c))
