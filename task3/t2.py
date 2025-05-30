import math

def f(x):
    if x > 3.5:
        return math.sin(x) * math.log10(x)
    elif x <= 3.5:
        return math.pow(math.cos(x), 2)
    else:
        return None

x = 2.0

# Заголовок таблиці
print(f"{'x':^10}|{'y':^15}")
print("-" * 26)

# Виведення значень
while x <= 5:
    y = f(x)
    print(f"{x:^10.2f}|{y:^15.6f}")
    x += 0.25