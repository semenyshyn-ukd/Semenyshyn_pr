print("First task")
nums = []
while True:
    input_num = int(input("Input number(greater than 6 and when divided by 5 there is a remainder of 2): "))
    if input_num > 6 and input_num % 5 == 2:
        nums.append(input_num)
        print("Number append to array!")
    else:
        print("Input incorrect!")
    if len(nums) == 10:
        break

print("\nSecond task")
even = []
odd = []
for el in nums:
    if el % 2 != 0:
        odd.append(el)
        odd.sort(reverse=False)
    if el % 2 == 0:
        even.append(el)
print(odd)
print(f"Min num: {min(even)} \nMax num: {max(even)}")

print("\nThird task")
multi = 1
sum_el = 0
count_plus = 0
count_minus = 0
for el in nums:
    if el >= 0:
        multi *= el
        count_plus += 1
    if el <= 0:
        count_minus += 1
    sum_el += el
print(f"Count positive numbers: {count_plus} \nMultiply positive numbers: {multi}")
print(f"\nCount negative numbers: {count_minus}")
print(f"Arithmetic mean: {sum_el / len(nums)}")