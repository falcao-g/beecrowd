import sys
values = [int(x) for x in sys.stdin.readline().split()]
sys.stdout.write(str(max(values))+'\n')