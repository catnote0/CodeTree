n, m, r, c = map(int, input().split())
directions = list(input().split())

top, front, right, left, back, bottom = 1, 2, 3, 4, 5, 6
move = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
grid = [[0] * n for _ in range(n)]
r -= 1
c -= 1
grid[r][c] = bottom

def roll(drc):
    global top, front, right, left, back, bottom, r, c
    dr, dc = move[drc]
    if r + dr < 0 or r + dr >= n or c + dc < 0 or c + dc >= n: return
    r, c = r + dr, c + dc
    if drc == 'L': top, front, right, left, back, bottom = right, front, bottom, top, back, left
    if drc == 'R': top, front, right, left, back, bottom = left, front, top, bottom, back, right
    if drc == 'U': top, front, right, left, back, bottom = front, bottom, right, left, top, back
    if drc == 'D': top, front, right, left, back, bottom = back, top, right, left, bottom, front

for drc in directions:
    roll(drc)
    grid[r][c] = bottom

print(sum(sum(row) for row in grid))