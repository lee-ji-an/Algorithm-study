import sys


def solution(relationships, target, limit):
    from collections import defaultdict, deque
    ans = 0
    adj = defaultdict(list)
    for rel in relationships:
        adj[rel[0]].append(rel[1])
        adj[rel[1]].append(rel[0])

    visited = [False] * 101
    visited[target] = True
    queue = deque([(target, 0)])
    for friend in adj[target]:
        if not visited[friend]:
            visited[friend] = True
            ans += 5
            queue.append((friend, 1))
    # print(ans)
    while queue:
        friend, cnt = queue.popleft()
        if cnt >= limit:
            break
        for f in adj[friend]:
            if not visited[f]:
                # print(f, cnt)
                ans += 11
                visited[f] = True
                queue.append((f, cnt + 1))
    return ans


print(solution([[1, 2], [2, 3], [2, 6], [3, 4], [4, 5]], 1, 2))
