#Personal Information & Simple Calculator

#1. Ask the user for their name
name = input("Enter your name: ")

#2. Ask for their age
print()
age = int(input("Enter your age: "))

#3. Ask for two numbers
print()
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter second number: "))

#4. Calculate the sum, subtraction, multiplication, and division of those two numbers
sum = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

#5. Display all information in a well-formatted output using f-strings
print()
print(f"Hello, {name}!")
print(f"Age: {age}")

print()
print(f"Addition: {sum}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")