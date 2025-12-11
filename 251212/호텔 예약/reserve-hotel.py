n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]
s = [interval[0] for interval in intervals]
e = [interval[1] for interval in intervals]

List = []
for s, e in intervals:
    List.append((s, 1))
    List.append((e + 0.1, -1))
List.sort()

Count = 0
Result = 0
for p, c in List:
    Count += c
    Result = max(Result, Count)

print(Result)