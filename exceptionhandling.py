# Task 39: Exception Handling
# Example 1: ZeroDivisionError
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Please enter numbers only!")
# Example 2: FileNotFoundError
try:
    with open("sample.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found!")
# Example 3: IndexError
try:
    numbers = [10, 20, 30]
    index = int(input("Enter index (0-2): "))
    print(numbers[index])
except IndexError:
    print("Invalid index!")
except ValueError:
    print("Enter a valid integer!")
# Example 4: Finally block
try:
    num = int(input("Enter a number: "))
    print("Square:", num ** 2)
except ValueError:
    print("Invalid input!")
finally:
    print("Program completed!")