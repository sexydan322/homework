n = int(input("Введите длину"))
for i in range(1, n * 2, 2):
    print(('*' * i).center(n * 2))
