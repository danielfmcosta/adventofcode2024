from collections import defaultdict


with open('input.txt', 'r') as f:
    s = f.read().strip()

garden = [list(r) for r in s.split('\n')]
n, m = len(garden), len(garden[0])

visited  = {}
def dfs(x, y, crop, i):
    if x in range(n) and y in range(m):
        if (x, y) in visited:
            return 
        if garden[x][y] == crop:
            visited[(x, y)] = i
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                dfs(x + dx, y + dy, crop, i)

next=0
for i in range(n):
    for j in range(m):
        if (i, j) not in visited:
            dfs(i, j, garden[i][j], next)
            next += 1

visited_inv = defaultdict(set)
for k, v in visited.items():
    visited_inv[v].add(k)


ans = 0
for visited, nodes in visited_inv.items():
    area = len(nodes)
    per = []
    for n0 in nodes:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = n0[0] + dx, n0[1] + dy
            if nx not in range(n) or ny not in range(m) or (nx, ny) not in nodes:
                per.append((n0, (nx, ny)))
    per = set(per)
    final_per = set()
    for p1, p2 in per:
        keep = True
        for dx, dy in [(1, 0), (0, 1)]:
            p1n = (p1[0] + dx, p1[1] + dy)
            p2n = (p2[0] + dx, p2[1] + dy)
            if (p1n, p2n) in per:
                keep = False
        if keep:
            final_per.add((p1, p2))
    ans += (area * (len(final_per)))

print(ans)

