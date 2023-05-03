message = input()

words = message.split()
decoded = []

for word in words:
    new_word = ""
    for i in range(len(word)):
        if i % 2 != 0:
            new_word += word[i]
    decoded.append(new_word)

print(' '.join(decoded))