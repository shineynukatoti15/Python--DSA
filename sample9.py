number = int(input("Enter a digit: "))
num2 = int(input("Enter the second digit: "))
print("Choose the symbol to perform the operation:")
symbol = input("Enter the symbol: ")

if symbol == '+':
    print("Addition is:", number + num2)
elif symbol == '-':
    print("Subtraction is:", number - num2)
elif symbol == '*':
    print("Multiplication is:", number * num2)
elif symbol == '/':
    print("Division is:", number / num2)
else:
    print("Invalid operator")