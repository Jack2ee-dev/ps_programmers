def solution(genres, plays):
    answer = []

    g_dict = dict()
    for i in range(len(genres)):
        if genres[i] in g_dict:
            g_dict[genres[i]]["plays"] += plays[i]
            g_dict[genres[i]]["songs"].append({
                "index": i,
                "play": plays[i]
            })
        else:
            g_dict[genres[i]] = dict({
                "plays": plays[i],
                "songs": [{
                    "index": i,
                    "play": plays[i]
                }]
            })

    g_order = []
    for gk in g_dict.keys():
        g_order.append(g_dict[gk])

    g_order.sort(key=lambda x: -x["plays"])
    for g in g_order:
        if len(g["songs"]) <= 1:
            answer.append(g["songs"][0]["index"])
        else:
            g["songs"].sort(key=lambda x: -x["play"])
            answer.append(g["songs"][0]["index"])
            answer.append(g["songs"][1]["index"])

    return answer


def solution2(genres, plays):
    ht1 = dict()
    ht2 = dict()

    for i, elem in enumerate(zip(genres, plays)):
        g, p = elem
        print(elem)
        if g not in ht1:
            ht1[g] = 0
            ht2[g] = []
        ht1[g] += p
        ht2[g].append((i, p))

    sort_ht1 = sorted(list(ht1.items()), key=lambda x: -x[1])

    answer = []
    for g, p in sort_ht1:
        sort_ht2 = sorted(ht2[g], key=lambda x: -x[1])
        answer += list(map(lambda x: x[0], sort_ht2))[:2]
    # stable한 sort아미로 인덱스 기준 정렬이 필요없음

    return answer


if __name__ == "__main__":
    print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
    solution2(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
