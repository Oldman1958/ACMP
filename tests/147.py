def fibonacci(n):
    if n == 0:
        return 0
    elif n in (1, 2):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input())
print(fibonacci(n))
