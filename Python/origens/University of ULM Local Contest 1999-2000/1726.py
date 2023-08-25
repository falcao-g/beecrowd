def evaluate(exp):
    new = ''
    pending = False
    for c in exp:
        if c.isalpha():
            new += f'"{c}",'
        elif c == '{' or c == '(' or c == ')':
            new += c
        elif c == '}':
            if new[-1] == ',':
                new = new[:-1]
            new += c
            if pending:
                new += ')'
                pending = False
        elif c == '+':
            new += '.union('
            pending = True
        elif c == '-':
            new += '.difference('
            pending = True
        elif c == '*':
            new += '.intersection('
            pending = True

    return new

def priority(exp):
    if '.intersection(' in exp and ('.union(' in exp or '.difference(' in exp):
        while '.intersection(' in exp:
            start = 0
            end = 0
            for i in range(len(exp)-1):
                if exp[i] == '.':
                    if exp[i+1] == 'i':
                        for j in range(i, 0, -1):
                            if exp[j] == '{':
                                start = j
                                break
                            elif exp[j] == ')':
                                if exp[j-1] == ')':
                                    return exp
                                else:
                                    exp = exp[0:j] + exp[j+1:]
                        for j in range(i, len(exp)):
                            if exp[j] == ')':
                                end = j
                                break
                        break
            exp = exp[0:start] + str(eval(exp[start:end+1])) + exp[end:]
        
    return exp

import sys

while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    result = eval(priority(evaluate(line)))
    answer = '{' + ''.join(sorted(result)) + '}'
    sys.stdout.write(f'{answer}\n')

