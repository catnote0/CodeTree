n, k = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = -1
one = 0
Result = 0x7FFFFFFF

while True:
    if one < k:
        right += 1
        if right == n: break;
        if arr[right] == 1: one += 1
    else:
        Result = min(Result, right - left + 1)
        if arr[left] == 1: one -= 1
        left += 1

print(-1 if Result == 0x7FFFFFFF else Result)
