a = int(input("Количество учеников в первом классе?"))
b = int(input("Количество учеников во втором классе?"))
c = int(input("Количество учеников в третем классе?"))

d = a + b + c

e = d // 2 + d % 2

print("Такое количество парт надо закупить", e)