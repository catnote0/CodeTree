n = int(input())
numbers = [int(input()) for _ in range(n)]

inf = 0x7FFFFFFF
mod = [-1] + [inf] * 6

Sum = 0
Result = 0
for i, num in enumerate(numbers):
    Sum += num
    if mod[Sum % 7] == inf: mod[Sum % 7] = i
    else: Result = max(Result, i - mod[Sum % 7])

print(Result)