n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

position = [1] * k
max_score = 0

def move(num):
    global max_score
    if num == n:
        score = sum(1 if pos >= m else 0 for pos in position)
        max_score = max(max_score, score)
        return
    for i in range(k):
        position[i] += nums[num]
        move(num + 1)
        position[i] -= nums[num]

move(0)

print(max_score)