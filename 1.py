lst = [[0 for _ in range(2)] for _ in range(3)]

lst[0:1][0:1] = 1
print(lst)
