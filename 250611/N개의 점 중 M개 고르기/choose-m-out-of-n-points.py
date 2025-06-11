n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]
result = 0x7FFFFFFF

def dist(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

def select(now_num, cnt, plist):
    global result
    if cnt == m:
        maxdist = 0
        for i in range(cnt):
            for j in range(i + 1, cnt): maxdist = max(maxdist, dist(plist[i], plist[j]))
        result = min(result, maxdist)
    if now_num == n: return
    select(now_num + 1, cnt + 1, plist + [points[now_num]])
    select(now_num + 1, cnt, plist)

select(0, 0, [])
print(result)