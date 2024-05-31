def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b


print(calculator(float(input('Enter A : ')), float(input('Enter B : ')), str(input('Enter OP : '))))
