n = int(input())
Result = 0

def select(num):
    global Result
    if num > n: return
    if num == n: Result += 1
    for i in range(1, 5): select(num + i)

select(0)
print(Result)