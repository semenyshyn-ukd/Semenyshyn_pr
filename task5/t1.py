import random

array = []
n = int(input("Enter a count of elements: "))
for i in range(n):
    array.append(random.randrange(-99, 101))
print(array)

odd = []
for index, el in enumerate(array):
    if el < 0:
        odd.append(index)
        if len(odd) == 2:
            break
if len(odd) < 2:
    print("In list less than 2 elements")
else:
    start = odd[0]
    end = odd[1]
    suma = sum(array[start + 1:end])
    print(f"Sum of elements between {array[start]} and {array[end]}: {suma}")