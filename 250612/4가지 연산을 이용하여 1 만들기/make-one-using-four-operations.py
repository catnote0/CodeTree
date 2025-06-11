N = int(input())
MAX_DIST = 0x7FFFFFFF
MAX_NUM = 5000000
Distance = [MAX_DIST] * MAX_NUM

if N == 1:
    print(0)
    exit(0)

Distance[N] = 0
Queue = [N]
T = 0
while True:
    T += 1
    tmpQueue = []
    for x in Queue:
        if T < Distance[x - 1]:
            Distance[x - 1] = T
            tmpQueue.append(x - 1)
            if x - 1 == 1:
                print(T)
                exit(0)
        if x + 1 < MAX_NUM and T < Distance[x + 1]:
            Distance[x + 1] = T
            tmpQueue.append(x + 1)
        if x % 2 == 0 and T < Distance[x // 2]:
            Distance[x // 2] = T
            tmpQueue.append(x // 2)
            if x // 2 == 1:
                print(T)
                exit(0)
        if x % 3 == 0 and T < Distance[x // 3]:
            Distance[x // 3] = T
            tmpQueue.append(x // 3)
            if x // 3 == 1:
                print(T)
                exit(0)
    Queue = tmpQueue