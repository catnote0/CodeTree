n, m, k = map(int, input().split())

# Read grid as list of strings since we need character-by-character access
grid = [input() for _ in range(n)]

# Read k queries as tuples
queries = [tuple(map(int, input().split())) for _ in range(k)]

check = [[[0] * m for _ in range(n)] for _ in range(3)]
letter = ['a', 'b', 'c']

for i, l in enumerate(letter):
    for x in range(n):
        for y in range(m):
            if x > 0 or y > 0:
                if x == 0: check[i][x][y] = check[i][x][y - 1]
                elif y == 0: check[i][x][y] = check[i][x - 1][y]
                else: check[i][x][y] = check[i][x][y - 1] + check[i][x - 1][y] - check[i][x - 1][y - 1]
            check[i][x][y] += 1 if grid[x][y] == l else 0

for x1, y1, x2, y2 in queries:
    x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
    for i, l in enumerate(letter):
        Result = 0
        if x1 == 0 and y1 == 0: Result = check[i][x2][y2]
        elif x1 == 0: Result = check[i][x2][y2] - check[i][x2][y1 - 1]
        elif y1 == 0: Result = check[i][x2][y2] - check[i][x1 - 1][y2]
        else: Result = check[i][x2][y2] - check[i][x2][y1 - 1] - check[i][x1 - 1][y2] + check[i][x1 - 1][y1 - 1]
        print(Result, end = " ")
    print()