n = int(input())
grid = [list(input()) for _ in range(n)]

pos = [[] for _ in range(11)]
result = 0x7FFFFFFF

for i in range(n):
    for j in range(n):
        if grid[i][j].isdigit(): pos[ord(grid[i][j]) - 48] = (i, j)
        if grid[i][j] == 'S': pos[0] = (i, j)
        if grid[i][j] == 'E': pos[10] = (i, j)

def dist(a, b):
    return abs(pos[a][0] - pos[b][0]) + abs(pos[a][1] - pos[b][1])

def visit(now, cnt, distance):
    global result
    if distance > result: return
    if now == 10:
        if cnt < 5: return
        result = min(result, distance)
        return
    for i in range(now + 1, 11):
        if not pos[i]: continue
        visit(i, cnt + 1, distance + dist(now, i))

visit(0, 1, 0)
print(-1 if result == 0x7FFFFFFF else result)