n, m, c = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
Value = [0, 0]
Result = 0

def select(thief_num, x, y, num, weight, value):
    if weight > c: return
    if num == m:
        Value[thief_num] = max(Value[thief_num], value)
        return
    select(thief_num, x, y, num + 1, weight, value)
    select(thief_num, x, y, num + 1, weight + grid[x][y + num], value + grid[x][y + num] ** 2)

for x1 in range(n):
    for y1 in range(n - m + 1):
        for x2 in range(x1, n):
            for y2 in range(y1 + m if x1 == x2 else 0, n - m + 1):
                Value = [0, 0]
                select(0, x1, y1, 0, 0, 0)
                select(1, x2, y2, 0, 0, 0)
                Result = max(Result, sum(Value))

print(Result)