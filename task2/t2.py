import random

# Генеруємо рандомні числа
num1 = random.randint(1, 1001)
num2 = random.randint(1, 1001)
num3 = random.randint(1, 1001)
num4 = random.randint(1, 1001)
num5 = random.randint(1, 1001)

print(f"Згенеровані числа: {num1}, {num2}, {num3}, {num4}, {num5}")

# Початкові значення
total_sum = 0
count = 0

# Обробляємо num1
total_sum += num1
if num1 % 10 == 0:
    count += 1
    print(f"Число {num1} кратне 10")

# Обробляємо num2
total_sum += num2
if num2 % 10 == 0:
    count += 1
    print(f"Число {num2} кратне 10")

# Обробляємо num3
total_sum += num3
if num3 % 10 == 0:
    count += 1
    print(f"Число {num3} кратне 10")

# Обробляємо num4
total_sum += num4
if num4 % 10 == 0:
    count += 1
    print(f"Число {num4} кратне 10")

# Обробляємо num5
total_sum += num5
if num5 % 10 == 0:
    count += 1
    print(f"Число {num5} кратне 10")

print(f"Сума чисел: {total_sum}")
print(f"Кількість чисел кратних 10: {count}")