import random

# Формування чисел за допомогою рандомайзера
num1 = random.randint(1, 1001)
num2 = random.randint(1, 1001)
num3 = random.randint(1, 1001)
num4 = random.randint(1, 1001)
num5 = random.randint(1, 1001)

#Початкові значення для подальшого циклу
num0 = 0
count = 0

#Створення списку чисел
nums = [num1, num2, num3, num4, num5]

#Створення нескінченного циклу
while True:
    # Вибір дії
    choice = input(f"\n1. Робити дії над числами"
                   f"\n0. Вихід"
                   f"\nВаш вибір: ")

    if choice == '1':
        for num in nums:
            if num % 10 == 0:
                count += 1
            num0 += num

        print(f"Сума чисел: {num0}"
          f"\nК-сть чисел кратних 10: {count}")

    elif choice == '0':
        print("Вихід з програми")
        break

    else:
        print("Неправильний вибір")