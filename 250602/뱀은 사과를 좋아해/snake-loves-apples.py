from collections import deque

N, M, K = map(int, input().split())

grid = [[0] * N for _ in range(N)]
grid[0][0] = 'S'

for _ in range(M):
    x, y = map(int, input().split())
    grid[x - 1][y - 1] = 'A'

snake = deque([(0, 0)])
move = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
d, p = [], []
Time = 0
for _ in range(K):
    d, p = input().split()
    for _ in range(int(p)):
        Time += 1
        nx, ny = snake[-1][0] + move[d][0], snake[-1][1] + move[d][1]
        if nx < 0 or N <= nx or ny < 0 or N <= ny:
            print(Time)
            exit(0)
        if grid[nx][ny] != 'A':
            tx, ty = snake.popleft()
            grid[tx][ty] = 0
        if grid[nx][ny] == 'S':
            print(Time)
            exit(0)
        snake.append((nx, ny))
        grid[nx][ny] = 'S'

print(Time)