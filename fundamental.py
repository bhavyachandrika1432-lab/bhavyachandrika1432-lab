def square_all(numbers):
    return list(map(lambda x: x ** 2, numbers))

numbers = [2, 3, 4, 5]
result = square_all(numbers)
print(result)
def filter_positive(numbers):
    return list(filter(lambda x: x > 0, numbers))

numbers = [-5, 3, -2, 7, 0, 4]
result = filter_positive(numbers)
print(result)
from functools import reduce

def calculate_factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)

n = 5
result = calculate_factorial(n)
print(result)
from functools import reduce

def count_vowels(string):
    return reduce(lambda count, ch: count + (ch.lower() in "aeiou"), string, 0)

string = "Bhavya"
result = count_vowels(string)
print(result)