n = int(input())

def seq(now_seq, length):
    if length == n:
        print("".join(map(str, now_seq)))
        exit(0)
    for i in range(4, 7):
        now_seq.append(i)
        possible = True
        for j in range(2, length + 2, 2):
            if now_seq[-j:-j // 2] == now_seq[-j // 2:]:
                possible = False
                break
        if possible: seq(now_seq, length + 1)
        del now_seq[-1]
seq([], 0)