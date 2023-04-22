import sys
while True:
    try:
        num1, num2 = map(int, sys.stdin.readline().split())
    except:
        break
    sys.stdout.write(str(num1^num2)+'\n')