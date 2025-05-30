double_array = [[1, 2, 3], [4, 5, 6, 7]]
just_array = []

for row in double_array:
    for el in row:
        just_array.append(el)
print(f"Максимальне число: {max(just_array)}")