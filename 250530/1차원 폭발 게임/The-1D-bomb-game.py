n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

while True:
    if not numbers: break
    combo = 1
    for i in range(1, len(numbers)):
        if numbers[i - 1] == numbers[i]: combo += 1
        else:
            if combo >= m: numbers[i - combo:i] = [-1] * combo
            combo = 1
    if combo >= m: numbers[len(numbers) - combo:len(numbers)] = [-1] * combo
    if -1 not in numbers: break
    while -1 in numbers: numbers.remove(-1)

print(len(numbers))
for num in numbers: print(num)