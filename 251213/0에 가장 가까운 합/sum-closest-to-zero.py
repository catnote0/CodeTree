n = int(input())
a = list(map(int, input().split()))

a.sort()

left = 0
right = n - 1

Result = 0x7FFFFFFF
while left < right:
    Result = abs(left + right)
    if left + right > 0: right -= 1
    elif left + right < 0: left += 1
    else:
        print(0)
        exit(0)
print(Result)