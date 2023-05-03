import sys

def isTriangle(a, b, c):
    return a < b + c and b < a + c and c < a + b

varetas = [int(x) for x in sys.stdin.readline().split()]
sys.stdout.write(f"S\n" if isTriangle(varetas[0], varetas[1], varetas[2]) or isTriangle(varetas[0], varetas[1], varetas[3]) or isTriangle(varetas[0], varetas[2], varetas[3]) or isTriangle(varetas[1], varetas[2], varetas[3]) else f"N\n")