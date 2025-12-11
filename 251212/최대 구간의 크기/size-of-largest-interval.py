n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

End_List = []
for a, b in intervals:
    End_List.append((a, 1))
    End_List.append((b, -1))
End_List.sort()

left, right = 0, 0
Result = 0
Count = 0
for p, c in End_List:
    if Count == 0 and c == 1: left = p
    if Count == 1 and c == -1:
        right = p
        Result = max(Result, right - left)
    Count += c

print(Result)