n, k = map(int, input().split())
arr = list(map(int, input().split()))

Dict = {arr[0]: 1}
left = 0
right = 0
Result = 0

while right < n - 1:
    if arr[right + 1] in Dict and Dict[arr[right + 1]] == k:
        Dict[arr[left]] -= 1
        if Dict[arr[left]] == 0: del Dict[arr[left]]
        left += 1
    else:
        right += 1
        Dict[arr[right]] = 1 if arr[right] not in Dict else Dict[arr[right]] + 1
    Result = max(Result, right - left + 1)

print(Result)