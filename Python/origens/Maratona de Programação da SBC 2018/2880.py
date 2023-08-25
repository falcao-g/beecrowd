import sys

message = sys.stdin.readline().strip()
crib = sys.stdin.readline().strip()

length = len(crib)
positions = 0
for i in range(len(message) - length + 1):
    flag = True
    section = message[i:i+length]

    for c in range(length):
        if section[c] == crib[c]:
            flag = False
            break

    if flag:
        positions += 1

sys.stdout.write(f'{positions}\n')