def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    w_sum = 0
    unpassed = len(truck_weights)

    while True:
        if bridge[0] != 0:
            w_down = bridge.pop(0)
            w_sum -= w_down
            unpassed -= 1

            if len(truck_weights) > 0 and w_sum + truck_weights[0] <= weight:
                w_up = truck_weights.pop(0)
                w_sum += w_up
                bridge.append(w_up)
            else:
                bridge.append(0)
        else:
            if len(truck_weights) > 0 and w_sum + truck_weights[0] <= weight:
                bridge.pop(0)
                w_up = truck_weights.pop(0)
                bridge.append(w_up)
                w_sum += w_up
            else:
                bridge.append(bridge.pop(0))
        answer += 1
        if unpassed == 0:
            break

    return answer


if __name__ == "__main__":
    print(solution(2, 10, [7, 4, 5, 6]))
    print(solution(100, 100, [10]))
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
