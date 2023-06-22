def solution(s):
    answer = True
    stack = []

    for i in s:
        if i == "(":
            stack.append("(")
        else:
            if len(stack) == 0:
                return False
            stack.pop(-1)

    if len(stack) != 0:
        return False

    return True
