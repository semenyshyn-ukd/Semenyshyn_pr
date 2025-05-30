import math

def input_data():
    x = int(input("Enter value of x: "))
    y = int(input("Enter value of y: "))
    z = int(input("Enter value of z: "))

    if x > 0 and y > 0:
        return x, y, z
    else:
        print("Values x and y must be positive.")
        return None

def p(x, y):
    return 1 / (math.pow(x, 2) + math.pow(y, 2))

def v(x, y, z):
    return math.pow(p(x, y), 2) * z

def show(v_res, p_res):
    print(f"\nResult function p(x, y) = {p_res}")
    print(f"Result function v(x, y, z) = p^2 * z = {v_res}")

if __name__ == "__main__":
    data = input_data()
    if data:
        x, y, z = data
        p_res = p(x, y)
        v_res = v(x, y, z)
        show(v_res, p_res)