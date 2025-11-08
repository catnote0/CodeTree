MAX = 1001

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

coordinate = [[0] * (MAX + 1) for _ in range((MAX + 1))]

top = [[0] * (MAX + 1) for _ in range((MAX + 1))]
bottom = [[0] * (MAX + 1) for _ in range((MAX + 1))]

lefttop = [[0] * (MAX + 1) for _ in range((MAX + 1))]
leftbottom = [[0] * (MAX + 1) for _ in range((MAX + 1))]
righttop = [[0] * (MAX + 1) for _ in range((MAX + 1))]
rightbottom = [[0] * (MAX + 1) for _ in range((MAX + 1))]

Xset = set()
Yset = set()

for x, y in points:
    coordinate[x][y] = 1
    Xset.add(x)
    Yset.add(y)

for i in range(1, MAX):
    for j in range(1, MAX):
        top[i][j] = top[i - 1][j] + coordinate[i][j]
        bottom[MAX - i][j] = bottom[MAX - i + 1][j] + coordinate[MAX - i][j]

for i in range(1, MAX):
    for j in range(1, MAX):
        lefttop[i][j] = lefttop[i][j - 1] + top[i - 1][j] + coordinate[i][j]
        righttop[i][MAX - j] = righttop[i][MAX - j + 1] + top[i - 1][MAX - j] + coordinate[i][MAX - j]
        leftbottom[MAX - i][j] = leftbottom[MAX - i][j - 1] + bottom[MAX - i + 1][j] + coordinate[MAX - i][j]
        rightbottom[MAX - i][MAX - j] = rightbottom[MAX - i][MAX - j + 1] + bottom[MAX - i + 1][MAX - j] + coordinate[MAX - i][MAX - j]

Result = 0x7FFFFFFF
for i in range(1, MAX):
    for j in range(1, MAX):
        if i in Xset or j in Yset: continue
        Result = min(Result, max(lefttop[i - 1][j - 1], righttop[i - 1][j + 1], leftbottom[i + 1][j - 1], rightbottom[i + 1][j + 1]))

print(Result)