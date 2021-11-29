a = int(input('Введите длину'))
for i in range(2 * a + 1):
    if i <= a:
        print(' ' * (a - i) + '*' * (i + 1) + '*' * i)
    else:
        if i == (a * 2):
            print(' ' * a + '*')
        else:
            print(' ' * (i - a) + '*', end='')
            print(' ' * (4 * a - 2 * i - 1) + '*')
