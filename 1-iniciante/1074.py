for i in range(int(input())):
    string = ''

    x = int(input())

    if x == 0:
        string += 'NULL'
    else:
        if x % 2 == 0:
            string += 'EVEN '
        else:
            string += 'ODD '
            
        if x > 0:
            string += 'POSITIVE'
        else:
            string += 'NEGATIVE'
            
    print(string)