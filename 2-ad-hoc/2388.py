total = 0

for i in range(int(input())):
    inter, vm = map(int, input().split())
    total += inter * vm

print(total)