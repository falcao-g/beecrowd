input()
import sys
values = [int(x) for x in sys.stdin.readline().split()]
div = sum(values) // 2
soma = 0
for i in range(len(values)):
    soma += values[i]
    if div == soma:
        sys.stdout.write(f"{i+1}\n")
        break