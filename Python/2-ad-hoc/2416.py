import sys
metros, pista = map(int, sys.stdin.readline().split())
sys.stdout.write(str(metros%pista)+'\n')