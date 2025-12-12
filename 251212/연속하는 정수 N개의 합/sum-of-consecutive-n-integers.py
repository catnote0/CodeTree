n, m = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = -1
Sum = 0
Count = 0

while True:
    if Sum < m:
        right += 1
        if right == n: break
        Sum += arr[right]
    else:
        if Sum == m: Count += 1
        Sum -= arr[left]
        left += 1

print(Count)