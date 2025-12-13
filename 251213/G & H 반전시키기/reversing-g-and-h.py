N = int(input())
a = input()
b = input()

Count = 0
for i in range(N):
    if a[i] != b[i] and (i == 0 or a[i - 1] == b[i - 1]): Count += 1

print(Count)
