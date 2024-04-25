conj = set()

while True:
    try:
        s = input()
        conj.add(s)
    except:
        break

print(len(conj))
