N = int(input())
a = input()
b = input()

Count = 0
Start = -1
for i in range(N):
    if a[i] != b[i] and (i == 0 or a[i - 1] == b[i - 1]): Start = i
    if a[i] != b[i] and (i == N - 1 or a[i + 1] == b[i + 1]): Count += (i - Start) // 4 + 1

print(Count)
