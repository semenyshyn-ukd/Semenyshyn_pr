import random

#Формування чисел за допомогою рандомайзера
num1 = random.randint(1, 1001)
num2 = random.randint(1, 1001)
num3 = random.randint(1, 1001)

#Вивід створених чисел
print(f'\nNumber 1 is {num1}'
      f'\nNumber 2 is {num2}'
      f'\nNumber 3 is {num3}'
      f'\n')

#Визначення і вивід найменшого
if num1 < num2 and num1 < num3:
    print(f"Smallest number is {num1}")

if num2 < num1 and num2 < num3:
    print(f"Smallest number is {num2}")

if num3 < num2 and num3 < num1:
    print(f"Smallest number is {num3}")