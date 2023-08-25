for i in range(int(input())):
    o, t = input().split()
    o = int(o)
    
    if t == '1T':
        if o <= 45:
            print(o)
        else:
            print(f'45+{o-45}')
    else:
        if o <= 45:
            print(o + 45)
        else:
            print(f'90+{o-45}')