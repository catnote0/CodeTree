n, m, repeat = map(int, input().split())
numbers_2d = [list(map(int, input().split())) for _ in range(n)]

if m == 1:
    print(0)
    exit(0)

def explode():
    for i in range(n):
        combo = 1
        for j in range(1, n):
            if numbers_2d[j - 1][i] == numbers_2d[j][i]: combo += 1
            else:
                if combo >= m:
                    for k in range(j - combo, j): numbers_2d[k][i] = 0
                combo = 1
        if combo >= m:
            for k in range(n - combo, n): numbers_2d[k][i] = 0

def drop():
    after_drop = [[0] * n for _ in range(n)]
    for i in range(n):
        pos = n - 1
        for j in range(n - 1, -1, -1):
            if not numbers_2d[j][i]: continue
            after_drop[pos][i] = numbers_2d[j][i]
            pos -= 1
    for i in range(n): numbers_2d[i] = after_drop[i][:]

def rotate():
    after_rotate = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n): after_rotate[j][n - i - 1] = numbers_2d[i][j]
    for i in range(n): numbers_2d[i] = after_rotate[i][:]

for _ in range(repeat):
    explode()
    drop()
    rotate()
    drop()

explode()
drop()

print(sum(sum(num != 0 for num in row) for row in numbers_2d))