x = int(input())

odds = []

for i in range(x+1):
    if not i % 2 == 0:
        odds.append(i)
        
for i in odds:
    print(i)