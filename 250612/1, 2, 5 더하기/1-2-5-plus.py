n = int(input())

Memo = [1] + [-1] * 1000

def search(num):
    if Memo[num] != -1: return Memo[num]
    result = 0
    if num >= 1: result += search(num - 1)
    if num >= 2: result += search(num - 2)
    if num >= 5: result += search(num - 5)
    Memo[num] = result % 10007
    return Memo[num]

search(n)
print(Memo[n])