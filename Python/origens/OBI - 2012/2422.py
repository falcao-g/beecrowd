import sys

length = int(sys.stdin.readline())

houses = []
for i in range(length):
    houses.append(int(sys.stdin.readline()
))
target = int(sys.stdin.readline())

left = 0
right = len(houses) - 1

while left < right:
    current_sum = houses[left] + houses[right]
    if current_sum == target:
        sys.stdout.write(f"{houses[left]} {houses[right]}\n")
        break
    elif current_sum < target:
        left += 1
    else:
        right -= 1
        