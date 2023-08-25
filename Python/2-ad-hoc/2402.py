import math
def isPossible(n):
    if n == 0 or n == 1:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
        
print('S' if not isPossible(int(input())) else 'N')