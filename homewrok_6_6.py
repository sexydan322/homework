a = int(input('Введите длину'))
for i in range(2 * a + 1):
    if i <= a:
        print(' ' * (a - i) + '*' * (i + 1) + '*' * i)
    else:
        if i == (a * 2):
            print(' ' * a + '*')
        else:
            print(' ' * (i - a) + '*', end='')
            print(' ' * (2 * a - i - 1) + '*' + ' ' * (2 * a - i - 1) + '*')