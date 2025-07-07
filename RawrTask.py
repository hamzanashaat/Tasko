def add(C, D):
    return C + D

result = add(10, 20)

def subtract(C, D):
    return C - D
result2 = subtract(20, 10)

def multiply(C, D):
    return C * D
result3 = multiply(10, 20)

operation = input("Enter +, -, or *:")

C = int(input("Enter first number:"))
D = int(input("Enter second number:"))
if operation == "+":
    print("Result:", add(C, D))
elif operation == "-":
    print("Result:", subtract(C, D))
elif operation == "*":
    print("Result:", multiply(C, D))