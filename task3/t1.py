import math

#Оголошення функції
def f(x):
    return math.atan(x)

A = 2 #початок відрізка
B = 7 #кінець відрізка
M = 15 #к-сть підінтервалів
H = (B - A) / M #відстань між точками

for i in range(M + 1):
    x = A + i * H
    y = f(x)
    print(f"x = {x:.2f}, arctg(x) = {y:.5f}")