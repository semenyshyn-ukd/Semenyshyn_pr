#Заповняємо шапку і дані
data = [
    ["№ п/п", "Табельний номер", "План", "Факт", "%"],
    [1, 12345, 150, 145, 96.7],
]

#Розбиваємо список на шапку та контент
headers = data[0]
rows = data[1:]

#Форматування та вивід таблиці
print("-" * (10 * len(headers) + 3 * (len(headers) - 1)))

for i, header in enumerate(headers):
    print(f"{header:^10}", end="")
    if i < len(headers) - 1:
        print(" | ", end="")
print()

print("-" * (10 * len(headers) + 3 * (len(headers) - 1)))

for row in rows:
    for i, value in enumerate(row):
        print(f'{value:^10}', end='')
        if i < len(row) - 1:
            print(" | ", end='')
print()