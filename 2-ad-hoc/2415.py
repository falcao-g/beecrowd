import sys
sys.stdin.readline()
a = map(int, sys.stdin.readline().split())

large_seq_len = 0
temp_seq_len = 0
x = None

for i in a:
    if x is None or x == i:
        temp_seq_len += 1
    else:
        if temp_seq_len > large_seq_len:
            large_seq_len = temp_seq_len
        temp_seq_len = 1
    x = i

if temp_seq_len > large_seq_len:
    large_seq_len = temp_seq_len

sys.stdout.write(f'{large_seq_len}\n')
