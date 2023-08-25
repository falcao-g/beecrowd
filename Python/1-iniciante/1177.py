max = int(input())

actual = 0
for i in range(1000):
    print(f"N[{i}] = {actual}")
    if actual + 1 == max:
        actual = 0
    else:
        actual += 1