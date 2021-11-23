a = int(input("Введите число"))

b = 0

c = 0

while a != 0:
    a = int(input())

    c = 0

    while a != 0:

        a = int(input())

        if (a % 2) == 0:

            b += 1

        else:

            c += 1

    print("четные-", b, ",", "нечетные-", c)

    b += 1


print("количество введённых чисел", b)

