a = set()
b = set(n for n in range(1, 10001))
for i in b:
    for j in str(i):
        i += int(j)
    a.add(i)

c = sorted(b-a)
print(*c, sep="\n")
