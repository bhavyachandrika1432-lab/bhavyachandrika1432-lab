def add(a,b):
    return a+b
print(add(10,20))
def square(x):
    return x*x
print(square(19))
def factorial(n):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result
print(factorial(5))
def maximum(numbers):
    return max(numbers)
print(maximum([10,25,9,17]))
def reverse(s):
    return s[::-1]
print(reverse("python"))
def is_prime(n):
    if n>2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
        return True
print(is_prime(7))
def fibonacci(n):
    a=0
    b=1
    for i in range(n):
        a,b=b,a+b
    return a
print(fibonacci(7))
def is_palindrome(s):
    return s== s[::-1]
print(is_palindrome("madam"))
def sum_of_squares(numbers):
    total=0
    for num in numbers:
        total=total+num*num
    return total
print(sum_of_squares([1,2,3,4]))
def average(numbers):
    return sum(numbers)/len(numbers)
print(average([10,20,30,40]))