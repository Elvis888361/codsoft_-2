# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Get user input for numbers and operation
while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose operation (+, -, *, /): ")

        if operation not in ('+', '-', '*', '/'):
            raise ValueError("Invalid operation. Please choose +, -, *, or /.")

        break
    except ValueError as e:
        print(e)
        continue

# Perform the calculation and display the result
if operation == '+':
    result = add(num1, num2)
elif operation == '-':
    result = subtract(num1, num2)
elif operation == '*':
    result = multiply(num1, num2)
elif operation == '/':
    result = divide(num1, num2)

print(f"Result: {result}")
