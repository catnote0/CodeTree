N, K = map(int, input().split())
M = []
dir = []

for _ in range(N):
    m, d = input().split()
    M.append(int(m))
    dir.append(d)

End_Dict = dict()

last = 0
for i in range(N):
    left, right = 0, 0
    if dir[i] == 'L':
        left = last - M[i]
        right = last
        last = left
    else:
        left = last
        right = last + M[i]
        last = right
    End_Dict[left] = 1 if left not in End_Dict else End_Dict[left] + 1
    End_Dict[right] = -1 if right not in End_Dict else End_Dict[right] - 1

End_List = []
for key, value in End_Dict.items(): End_List.append((key, value))
End_List.sort()

Result = 0
Count = 0
for i in range(len(End_List)):
    if Count >= K: Result += (End_List[i][0] - End_List[i - 1][0])
    Count += End_List[i][1]

print(Result)