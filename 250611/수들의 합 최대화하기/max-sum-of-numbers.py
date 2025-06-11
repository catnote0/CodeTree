n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

column = [False] * n
result = 0

def select(row, now_sum):
    global result
    if row == n:
        result = max(result, now_sum)
        return
    for i in range(n):
        if column[i]: continue
        column[i] = True
        select(row + 1, now_sum + grid[row][i])
        column[i] = False

select(0, 0)
print(result)