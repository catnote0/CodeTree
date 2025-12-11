n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

List = []
for a, b in intervals:
    List.append((a, 1))
    List.append((b, -1))
List.sort()

Result = 0
Count = 0
for p, c in List:
    Count += c
    Result = max(Result, Count)

print(Result)