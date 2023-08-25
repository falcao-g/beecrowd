import sys

while True:
    try:
        num = int(sys.stdin.readline())
        if num == 1:
            print(0)
        else:
            print(int(num.bit_length() - 1))
    except:
        break