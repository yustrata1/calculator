first = float(input("Enter your first number: "))
second = float(input("Enter your second number: "))
operation = input("Enter sign of operation: ")
result = 0
if operation == "+":
    result = first + second
elif operation == "-":
    result = first - second
elif operation == "*":
    result = first * second
elif operation == "/":
    if first != 0 and second != 0:
        result = first / second
    else:
        print("0 is found, operation is incorrect")

else:
    print("Unknown operation")
print(result)
