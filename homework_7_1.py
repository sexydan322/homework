a = {}
for i in range(int(input())):
    for word in input().split():
        a[word] = a.get(word, 0) + 1

for i in sorted(a.items(), key=lambda x: (x[0])):
    if i[1] == max(a.values()):
        print(i[0])
        break

