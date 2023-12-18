import sys

N = int(sys.stdin.readline())
columns = ["X" for _ in range(N)]
column = 0
row = 0

for _ in range(N):
    str = sys.stdin.readline().strip()
    lst = str.split("X")
    for val in lst:
        if len(val) >= 2:
            row+=1
    
    for i in range(len(str)):
        columns[i] += str[i]

for st in columns:
    lst = st.split("X")
    for val in lst:
        if (len(val))>=2:
            column+=1

print(row, column)