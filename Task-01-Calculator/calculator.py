print("Simple Calculator")
def add(a, b):
  return a+b
def subtract(a, b):
  return a-b
def multiply(a, b):
  return a*b
def divide(a, b):
  if b==0:
    return "Oops Cannot divide by zero."
  return a/b
while True:
  print("\nChoose an Operation")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Exit")
  choice = input("Enter your choice (1-5): ")
  if choice=="1":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = add(num1, num2)
    print("Result = ", result)
  elif choice=="2":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = subtract(num1, num2)
    print("Result = ", result)
  elif choice=="3":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = multiply(num1, num2)
    print("Result = ", result)
  elif choice=="4":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = divide(num1, num2)
    print("Result = ", result)
  elif choice=="5":
    print("Thank you!")
    break
  else:
    print("Invalid choice.")