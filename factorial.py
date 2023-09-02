def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Test the function
num = int(input("Enter a number: "))
result = factorial_recursive(num)
print(f"The factorial of {num} is {result}")