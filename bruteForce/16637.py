import sys

# 연산자 우선순위는 모두 동일하기 때문에, 수식을 계산할 때는 왼쪽에서부터 순서대로 계산
# 중첩된 괄호는 사용할 수 없다
# 괄호를 적절히 추가해 만들 수 있는 식의 결과의 최댓값을 구하는 프로그램

N = int(sys.stdin.readline())
opr = list(sys.stdin.readline().strip())
result = -float('inf')

def calc(num1, op, num2):
    num1 = int(num1)
    num2 = int(num2)
    
    if op == "+":
        return num1 + num2
    
    elif op == "-":
        return num1 - num2
    
    else:
        return num1 * num2

def dfs(idx, prev):
    global result

    if idx >= N:
        result = max(result, prev)
        return 
    
    # 괄호 계산
    if idx + 3 <= N:
        dfs(idx+4, calc(prev, opr[idx], calc(opr[idx+1], opr[idx+2], opr[idx+3])))
    
    # 괄호 없는 계산
    dfs(idx + 2, calc(prev, opr[idx], opr[idx+1]))


if N == 1:
    result = int(opr[0])
else:
    dfs(1, opr[0])

print(result)
    