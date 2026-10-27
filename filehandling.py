# Task 37: File Handling
import os
folder = "file_handling"
os.makedirs(folder, exist_ok=True)
file_path = os.path.join(folder, "sample.txt")
# Write mode
with open(file_path, "w") as file:
    file.write("Welcome to Python File Handling\n")
# Read mode
with open(file_path, "r") as file:
    print("Read mode:")
    print(file.read())
# Append mode
with open(file_path, "a") as file:
    file.write("This is append mode\n")
# Read and write mode
with open(file_path, "r+") as file:
    print("r+ mode:")
    print(file.read())
    file.write("Added using r+ mode\n")
# Write and read mode
with open(file_path, "w+") as file:
    file.write("This is w+ mode\n")
    file.seek(0)
    print("w+ mode:")
    print(file.read())
# Append and read mode
with open(file_path, "a+") as file:
    file.write("This is a+ mode\n")
    file.seek(0)
    print("a+ mode:")
    print(file.read())