import math

def distance(x1, y1, x2, y2):
    if type(x1) is int and type(y1) is int and type(x2) is int and type(y2) is int:
        return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    else:
        print("Value must be numeric!")
        return 0

def herone(x1, y1, x2, y2, x3, y3):
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x3, y3, x1, y1)
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

if __name__ == '__main__':
    x1, y1 = 0, 0
    x2, y2 = 4, 0
    x3, y3 = 0, 3
    area = herone(x1, y1, x2, y2, x3, y3)
    print(f"Area of triangle: {area:.2f}")