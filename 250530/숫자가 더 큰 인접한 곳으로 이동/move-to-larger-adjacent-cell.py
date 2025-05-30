n, r, c = map(int, input().split())
a = [[0] * (n + 2) for _ in range(n + 2)]
drc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
Result = []

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        a[i][j] = row[j - 1]

def search(x, y):
    Result.append(a[x][y])
    for dx, dy in drc:
        if a[x + dx][y + dy] > a[x][y]:
            search(x + dx, y + dy)
            break
            
search(r, c)
print(*Result)