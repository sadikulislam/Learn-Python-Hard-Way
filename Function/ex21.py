def add(a, b):
    print(f"adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"subtructing {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"multiplying {a} * {b}")
    return a * b

def divide(a, b):
    print(f"dividing {a} / {b}")
    return a / b

print("Let's do some math with just functions!")
age = add(18, 7)
height = subtract(95, 10)
weight = multiply(82, 2)
iq = divide(90, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Let's fun!")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("That becomes: ", what, "Can you do it by hand?")