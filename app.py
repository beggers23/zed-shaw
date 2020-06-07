def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


age = add(30, 5)
height = subtract(74, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}\nHeight: {height}\nWeight: {weight}\nIQ: {iq}")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
form = (30 + (74 - (90 * (100 / 2))))
print(f"What? {what}")
print(f"Form? {form}")
