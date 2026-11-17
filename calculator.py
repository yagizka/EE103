def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
def calculator(operation, a, b):
    return operation(a, b)

print(calculator(add, 3, 5), add(3, 5))              # 8 8
print(calculator(subtract, 3, 5), subtract(3, 5))    # -2 -2
print(calculator(multiply, 3, 5), multiply(3, 5))    # 15 15
print(calculator(divide, 3, 5), divide(3, 5))        # 0.6 0.6