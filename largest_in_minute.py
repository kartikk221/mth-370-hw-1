import sys
import time

# We need to do this because output factorial is very large
sys.set_int_max_str_digits(100000000)

n = 0
factorial = 1
start_time = time.time()

while True:
    # Base factorial case
    if n == 0 or n == 1:
        factorial = 1
    else:
        factorial *= n

    # Increment the number
    n += 1

    # Check elapsed time after each iteration
    if time.time() - start_time > 60:
        break

# Print the result
print(f"Largest computable factorial in under 1 minute: {n - 1}!")
print(f"Time elapsed: {time.time() - start_time} seconds")
print(f"{n - 1}! = a number that is {len(str(factorial))} digits long")