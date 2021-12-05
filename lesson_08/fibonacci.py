
def fibonacci(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    for x in range(10):
        print(fibonacci(x))