import sys
from collections import deque

infix = sys.stdin.readline().strip()
stack = []
opr = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0, ')': 0}
result = []

def opr_func(c):
    # ) 닫는괄호일 때
    if c == ')':
        while stack:
            opt = stack.pop()
            if opt == '(':
                break
            result.append(opt)
    # ( 여는 괄호일 때
    elif c == '(':
        stack.append('(')

    # 그 외 연산자일 때
    else:
        # 스택 top에 있는 연산자가 우선순위가 크거나 같으면 pop한 후 push, 아니면 바로 push
        if len(stack) > 0:
            while stack:
                top = stack.pop()
                if opr[top] >= opr[c]:
                    result.append(top)
                else:
                    stack.append(top)
                    break
            stack.append(c)
        # 스택이 비었을 때
        else:
            stack.append(c)

for i in infix:
    if i in opr.keys():
        opr_func(i)
    else:
        result.append(i)

while stack:
    result.append(stack.pop())

for k in result:
    print(k, end='')