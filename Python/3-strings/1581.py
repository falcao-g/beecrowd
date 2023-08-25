for i in range(int(input())):
    p = int(input())
    langs = set()
    for j in range(p):
        langs.add(input())
    print('ingles' if len(langs) > 1 else langs.pop())
