import sys
sys.stdin.readline()
coded_message = sys.stdin.readline().split()

uncoded = ''
for word in coded_message:
    if len(word) > 3:
        uncoded += f'{word} '
    elif word.startswith('UR'):
        uncoded += 'URI '
    elif word.startswith('OB'):
        uncoded += 'OBI '
    else:
        uncoded += f'{word} '

sys.stdout.write(f'{uncoded[:-1]}\n')