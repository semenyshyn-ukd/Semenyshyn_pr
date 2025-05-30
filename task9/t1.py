import math

a0 = math.pi / 8
multi = a0
last_el = a0
n = 0

while True:
    n += 1
    last_el = last_el / math.sin(last_el)
    multi *= last_el
    if n == 5:
        break
print(multi)