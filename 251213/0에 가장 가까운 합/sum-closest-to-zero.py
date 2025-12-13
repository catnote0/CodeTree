n = int(input())
a = list(map(int, input().split()))

a.sort()

left = 0
right = n - 1

Result = 0x7FFFFFFF
while left < right:
    Result = min(Result, abs(a[left] + a[right]))
    if a[left] + a[right] > 0: right -= 1
    elif a[left] + a[right] < 0: left += 1
    else:
        print(0)
        exit(0)
print(Result)