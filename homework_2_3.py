a = int(input(":"))
a1 = (a % 10) * 100
a2 = int((a % 100) * 0.1)
a2 = a2 * 10
a3 = int(a * 0.01)
a4 = a1 + a2 + a3

print(a4)
