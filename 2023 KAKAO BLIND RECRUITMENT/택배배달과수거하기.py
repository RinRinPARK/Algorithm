# LV.2
# Greedy + Implementation(코드를 구현할 아이디어가 필요한 문제..)
# cap: 트럭에 실을 수 있는 재활용 택배 상자의 최대 개수를 나타내는 정수
# n: 배달할 집의 개수
# deliveries: 배달할 택배 상자 1차원 배열
# pickups: 수거할 택배상자 1차원 배열
def solution(cap, n, deliveries, pickups):
    # 끝에서부터 배달하고 끝에서부터 수거하기
    answer = 0
    
    d = 0
    p = 0
    for i in range(n-1, -1, -1):
        d += deliveries[i]
        p += pickups[i]
        while (d > 0) or (p > 0):
            d -= cap
            p -= cap
            answer += (i+1)*2
    
    return answer