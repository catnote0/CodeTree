n, m = map(int, input().split())
A = list(map(int, input().split()))
result = 0

def select(now, cnt, value):
    global result
    if cnt == m:
        result = max(value, result)
        return
    if now == n: return
    select(now + 1, cnt + 1, value ^ A[now])
    select(now + 1, cnt, value)

select(0, 0, 0)
print(result)