n = int(input())
num = [list(map(int, input().split())) for _ in range(n)]
move_dir = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
drc = [(), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
result = 0

def search(x, y, cnt):
    global result
    result = max(cnt, result)
    dx, dy = drc[move_dir[x][y]]
    now_num = num[x][y]
    while True:
        x, y = x + dx, y + dy
        if x < 0 or n <= x or y < 0 or n <= y: break
        if now_num < num[x][y]: search(x, y, cnt + 1)

search(r - 1, c - 1, 0)
print(result)