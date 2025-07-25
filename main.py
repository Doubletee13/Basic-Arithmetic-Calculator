'''
Basic Calculator that takes input of two numbers from the user and perform arithmetic operations with them
'''


# Declaring of two variables that will take input of floating numbers from the users

firstNumber = float(input("Enter first Number\n>>>> "))
secondNumber = float(input("Enter second Number\n>>> "))

total = firstNumber ** secondNumber
print(total)

#Modulus function implementation

firstNumber = float(input("Ennter First Number:\n>>"))
secondNumber = int(input("Enter second Number:\n>>"))

total = firstNumber % secondNumber
print(total)

#multiplication function

numb1 = float(input("Enter the first number you want to multiply: "))
numb2 = float(input("Enter the second number you want to multiply: "))

result = numb1 * numb2 


print(f"The result of {numb1} multiplied by {numb2} is equals to {result}")

#SUBTRACTION FUNCTION

number1 = float(input("Enter the first number you want to sub: "))
number2 = float(input("Enter the second number you want to sub: "))

answer = number1 - number2

print(answer)

