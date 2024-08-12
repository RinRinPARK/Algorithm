import sys
# -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cntn1 = 0
cnt0 = 0
cnt1 = 0

def curr(a, b, n): 
    global cntn1, cnt0, cnt1

    color = paper[a][b]

    for i in range(a, a + n):
        for j in range(b, b + n):

            if color != paper[i][j]:

                for x in range(3):
                    for y in range(3):

                        curr(a + x*n//3, b + y*n//3, n//3)
                return
            
    if color == -1:
        cntn1 += 1
    elif color == 0:
        cnt0 += 1
    else:
        cnt1 += 1

curr(0,0,N)
print(cntn1)
print(cnt0)
print(cnt1)