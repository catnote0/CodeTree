n = int(input())
num = list(map(int, input().split()))

Sum = sum(num)
result = Sum

def select(now_num, cnt, now_sum):
    global result
    if cnt == n:
        result = min(result, abs(Sum - now_sum * 2))
        return
    if now_num == n * 2: return
    select(now_num + 1, cnt + 1, now_sum + num[now_num])
    select(now_num + 1, cnt, now_sum)

select(0, 0, 0)
print(result)