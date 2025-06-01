n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
Result = 0
move = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
diagonal = [{}, {'R': 'U', 'U': 'R', 'L': 'D', 'D': 'L'}, {'R': 'D', 'D': 'R', 'L': 'U', 'U': 'L'}]

def pinball(x, y, drc):
    Time = 1
    while True:
        if x < 0 or n <= x or y < 0 or n <= y: return Time
        if grid[x][y] == 0: x, y = x + move[drc][0], y + move[drc][1]
        else:
            drc = diagonal[grid[x][y]][drc]
            x, y = x + move[drc][0], y + move[drc][1]
        Time += 1

for i in range(n):
    Result = max(Result, pinball(0, i, 'D'))
    Result = max(Result, pinball(n - 1, i, 'U'))
    Result = max(Result, pinball(i, 0, 'R'))
    Result = max(Result, pinball(i, n - 1, 'L'))

print(Result)