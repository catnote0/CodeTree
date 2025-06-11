n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

column = [False] * n
result = 0

def select(row, now_min):
    global result
    if row == n:
        result = max(result, now_min)
        return
    for i in range(n):
        if column[i]: continue
        column[i] = True
        select(row + 1, min(now_min, grid[row][i]))
        column[i] = False

select(0, 0x7FFFFFFF)
print(result)