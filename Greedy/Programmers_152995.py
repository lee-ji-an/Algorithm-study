def solution(scores):
    import heapq
    wanho = (scores[0][0], scores[0][1])
    sort_scores = sorted(scores, key=lambda x: (x[0], -x[1]))
    candidate = [(sort_scores[0][1], sort_scores[0][0])]

    prev = -1
    for i in range(1, len(sort_scores)):
        score_one, score_two = sort_scores[i][0], sort_scores[i][1]
        if score_one == prev:
            heapq.heappush(candidate, (score_two, score_one))
            continue
        while candidate and score_two > candidate[0][0]:
            employee = heapq.heappop(candidate)
            if employee[0] == wanho[1] and employee[1] == wanho[0]:
                return -1
        heapq.heappush(candidate, (score_two, score_one))
        prev = score_one

    total = [sum(cand) for cand in candidate]
    total.sort(reverse = True)
    ans = total.index(sum(wanho)) + 1

    return ans

