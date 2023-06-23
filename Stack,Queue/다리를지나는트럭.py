def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [truck_weights.pop(0)]
    length = [0]

    while len(bridge) > 0 or len(truck_weights) > 0:
        answer += 1
        for i in range(len(length)):
            length[i] += 1
        if length[0] > bridge_length:
            bridge.pop(0)
            length.pop(0)
        if len(truck_weights) != 0 and (len(bridge) < bridge_length) and ((sum(bridge)+truck_weights[0]) <= weight):
            truck = truck_weights.pop(0)
            bridge.append(truck)
            length.append(1)

    return answer
