a = input("Введите текст,пожалуйста")

b = a[:a.find('h') + 1]

c = a[a.find('h') + 1:a.rfind('h')]

f = a[a.rfind('h'):]

a = b + c.replace('h', 'H') + f

print(a)
