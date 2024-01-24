# LV.3
# Implementation + String
# 포화이진트리 노드개수 = 1 3 7 ... 2^n-1
# 포화이진트리로 만들기 -> 서브트리의 루트에 1이 아닌 것이 있는지 확인
import math

def check(left, right, bin_num):
    global flag
    if left == right:
        return
    
    mid = (left+right)//2
    
    if bin_num[mid] == '0':
        for i in range(left, mid):
            if bin_num[i] == '1':
                flag = 1
                return
        for j in range(mid+1, right+1):
            if bin_num[j] == '1':
                flag = 1
                return
    if flag == 0:
        check(left, mid-1, bin_num)
        check(mid+1, right, bin_num)


def solution(numbers):
    global flag
    answer = []
    
    for num in numbers:
        flag = 0
        bin_num = str(bin(num))[2:]
        # 포화 이진트리 형태로 만들기
        digit = 2 ** (int(math.log(len(bin_num), 2)) + 1) - 1
        bin_num = "0" * (digit - len(bin_num)) + bin_num
        
        # 루트가 0인 서브트리의 자식 노드의 값이 1이 되면 안됨
        check(0, len(bin_num)-1, bin_num)
        if flag == 0:
            answer.append(1)
        else:
            answer.append(0)
    
    return answer