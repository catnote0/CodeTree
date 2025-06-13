n = '0' + input()
mod = 1000000007
length = len(n) - 1
# Please write your code here.
DP = [[[0] * 2 for _ in range(3)] for _ in range(length + 1)]
# DP[i][j][k]: i번째 자리수까지 봤을 때 3으로 나눈 나머지가 j고,
# k는 N이랑 같은 숫자로 이어져 오는지 여부
# (k가 0이면 다음 d는 0~9에서 전개, 1이면 다음 d는 0~(N의 i+1번째 자리수)에서 전개

DP[0][0][1] = 1
# 0번째 가상 자리수 만들고 나머지는 0, k는 1인 상태로 초기값 설정

def get_rem(n):
    rem = 0
    for d in n: rem = (rem * 10 + int(d)) % mod
    return rem

rem = get_rem(n)

for i in range(length):
    next_digit = int(n[i + 1])
    for j in range(3):
        for d in range(10):
            if d in [3, 6, 9]: continue
            new_j = (j * 10 + d) % 3
            new_k = 0
            DP[i + 1][new_j][new_k] = (DP[i + 1][new_j][new_k] + DP[i][j][0]) % mod
        for d in range(next_digit + 1):
            if d in [3, 6, 9]: continue
            new_j = (j * 10 + d) % 3
            new_k = (d == next_digit)
            DP[i + 1][new_j][new_k] = (DP[i + 1][new_j][new_k] + DP[i][j][1]) % mod

not_clap_rem = sum(sum(row) for row in DP[length][1:]) % mod

result = rem - not_clap_rem
if result < 0: result += mod

print(result)