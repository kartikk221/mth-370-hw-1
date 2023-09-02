import time

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
print(f"Largest computable factorial in under 1 minute: {n - 1}")