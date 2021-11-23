a = [s for s in input("Введите ваш список").split()]
k = int(input("Введите 'id' элемента который вы хотите удалить"))

for i in range(k + 1, len(a)):
    a[i - 1] = a[i]

a.pop()

print(''.join([str(i) for i in a]))


