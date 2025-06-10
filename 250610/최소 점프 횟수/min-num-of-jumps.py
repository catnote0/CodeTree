n = int(input())
num = list(map(int, input().split()))
result = 100

def jump(pos, cnt):
    global result
    if pos >= n - 1:
        result = min(result, cnt)
        return
    for i in range(1, num[pos] + 1): jump(pos + i, cnt + 1)

jump(0, 0)
print(-1 if result == 100 else result)