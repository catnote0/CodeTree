n, s = map(int, input().split())
arr = list(map(int, input().split()))

Result = 0x7FFFFFFF
left = right = 0
Sum = arr[0]
while True:
    if Sum >= s:
        Result = min(Result, right - left + 1)
        Sum -= arr[left]
        left += 1
    else:
        right += 1
        if right >= n: break
        Sum += arr[right]

print(-1 if Result == 0x7FFFFFFF else Result)