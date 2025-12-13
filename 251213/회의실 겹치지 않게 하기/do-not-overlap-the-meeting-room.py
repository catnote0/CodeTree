n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

meetings.sort(key = lambda x: x[1])

count = 0
last = -1
for start, end in meetings:
    if start >= last:
        count += 1
        last = end

print(n - count)