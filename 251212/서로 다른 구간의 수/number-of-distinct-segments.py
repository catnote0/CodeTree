n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

List = []
for a, b in intervals:
    List.append((a, 1))
    List.append((b, -1))
List.sort()

Count = 0
Result = 0
for p, c in List:
    if Count == 0 and c == 1: Result += 1
    Count += c

print(Result)