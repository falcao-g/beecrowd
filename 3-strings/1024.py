import sys, itertools

for _ in itertools.repeat(None, int(sys.stdin.readline())):
    text = sys.stdin.readline()
    new_text = []

    for c in range(len(text)):
        if c < int(len(text)/2):
            if text[c].isalpha():
                new_text += chr(ord(text[c]) + 2)
            else:
                new_text += chr(ord(text[c]) - 1)
        else:
            if text[c].isalpha():
                new_text += chr(ord(text[c]) + 3)
            else:
                new_text += text[c]
    sys.stdout.write(''.join(new_text[-2::-1])+'\n')