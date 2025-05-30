import random

#Викликаємо рандомайзер для числа
number = random.randint(1, 101)

#Вивід інформації та число +- 1
print(f'\nNumber is {number}'
      f'\nNumber greater than one: {number + 1}'
      f'\nNumber less than one: {number - 1}')