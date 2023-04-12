x = int(input())
y = int(input())

inc = 1
if x > y:
    inc = -1

total = 0
for i in range(x, y+inc, inc):
    if i % 13 != 0:
        total += i

print(total)