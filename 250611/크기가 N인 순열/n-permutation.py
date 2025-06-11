n = int(input())
check = [False] * (n + 1)

def permu(cnt, plist):
    if cnt == n:
        print(*plist)
        return
    for i in range(1, n + 1):
        if not check[i]:
            check[i] = True
            permu(cnt + 1, plist + [i])
            check[i] = False

permu(0, [])