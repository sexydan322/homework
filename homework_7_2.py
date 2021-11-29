a = int(input("1 аргумент"))

b = int(input("2 аргумент"))

c = input("3 аргумент")

if c == "+":
    print(a, "+", b, "=", a + b)

elif c == "-":
    print(a, "-", b, "=", a - b)

elif c == "*":
    print(a, "*", b, "=, a*b")

elif c == "/":
    print(a, "/", b, "=", a / b)

else:
    print("Неизвестная операция")
