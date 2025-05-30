#Запитуємо користувача дані
user_name = input("Enter your name: ")
user_birthday_year = input("Enter your birthday year: ")

#Розраховуємо вік
age = 2025 - int(user_birthday_year)

#Вивід інформації
print(f'Name: {user_name} \nAge: {age}')