from collections import deque

x, y, z = map(int, input().split())
maximum_water = [x, y, z]
visit = [[False] * (x + 1) for _ in range(y + 1)]
ans = set()
q = deque()


def move(c, move_from, move_to):
    next_c = c.copy()
    next_c[move_to] = min(c[move_to] + c[move_from], maximum_water[move_to])
    next_c[move_from] = c[move_from] - min(maximum_water[move_to] - c[move_to], c[move_from])
    return next_c


q.append([0, 0, z])
visit[0][0] = True
while q:
    current = q.popleft()

    if current[0] == 0:
        ans.add(current[2])

    for i in range(0, 3):
        for j in range(0, 3):
            next_water = move(current, i, j)
            if i != j and not visit[next_water[1]][next_water[0]]:
                q.append(next_water)
                visit[next_water[1]][next_water[0]] = True

print(" ".join(map(str, sorted(ans))))