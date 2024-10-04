import sys

# 폭발 문자열이 폭발하면 그 문자는 문자열에서 사라지며, 남은 문자열은 합쳐지게 된다.

# 문자열이 폭발 문자열을 포함하고 있는 경우에, 모든 폭발 문자열이 폭발하게 된다. 
# 남은 문자열을 순서대로 이어 붙여 새로운 문자열을 만든다.
# 새로 생긴 문자열에 폭발 문자열이 포함되어 있을 수도 있다.
# 폭발은 폭발 문자열이 문자열에 없을 때까지 계속된다.

# 남아있는 문자가 없는 경우 "FRULA"를 출력

sentence = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()

stack = []

for sen in sentence:
    stack.append(sen)

    if (''.join(stack[-len(bomb):]) == bomb):
        for _ in range(len(bomb)):
            stack.pop()

if len(stack) != 0:
    print(*stack, sep="")
else:
    print("FRULA")