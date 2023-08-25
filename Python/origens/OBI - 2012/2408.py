import sys 
scores = [int(x) for x in sys.stdin.readline().split()]
scores.sort()
sys.stdout.write(str(scores[1]) + '\n')