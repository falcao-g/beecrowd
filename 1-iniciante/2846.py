def is_fibonacci(n):
    if n == 0 or n == 1:
        return True
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n

def find_nth_non_fibonacci(n):
    count = 0
    i = 0
    while count < n:
        if not is_fibonacci(i):
            count += 1
        i += 1
    return i-1

print(find_nth_non_fibonacci(int(input())))