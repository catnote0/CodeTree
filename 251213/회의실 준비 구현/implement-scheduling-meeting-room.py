n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

meetings.sort(key = lambda x: x[1])
last = -1
count = 0
for meeting in meetings:
    if meeting[0] >= last:
        count += 1
        last = meeting[1]

print(count)