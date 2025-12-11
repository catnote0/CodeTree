n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

End_List = []
for a, b in intervals:
    End_List.append((a, 1))
    End_List.append((b, -1))
End_List.sort()

Result = 0
Count = 0
for i in range(len(End_List)):
    if Count >= 1: Result += (End_List[i][0] - End_List[i - 1][0])
    Count += End_List[i][1]

print(Result)