class Node:
    def __init__(self, number):
        self.number = number
        self.prev = None
        self.next = None

N, M, Q = map(int, input().split())

circle_size = []
student_nums = []

for _ in range(M):
    nums = list(map(int, input().split()))
    circle_size.append(nums[0])
    student_nums.append(nums[1:])

command = []
A = []
B = []

for _ in range(Q):
    query = list(map(int, input().split()))
    command.append(query[0])
    A.append(query[1])
    if query[0] in [1, 2]: B.append(query[2])
    else: B.append(0)

node_list = dict()

for s_list in student_nums:
    for s in s_list: node_list[s] = Node(s)
    for i, s in enumerate(s_list):
        node_list[s].prev = node_list[s_list[i - 1]]
        node_list[s].next = node_list[s_list[(i + 1) % len(s_list)]]

for i in range(Q):
    if command[i] == 1:
        a, b = A[i], B[i]
        node_list[a].next.prev = node_list[b].prev
        node_list[b].prev.next = node_list[a].next
        node_list[a].next = node_list[b]
        node_list[b].prev = node_list[a]
    elif command[i] == 2:
        a, b = A[i], B[i]
        node_list[a].prev.next = node_list[b]
        node_list[b].prev.next = node_list[a]
        node_list[a].prev, node_list[b].prev = node_list[b].prev, node_list[a].prev
    else:
        a = A[i]
        Result, now = [a], a
        min_pos, pos = 0, 0
        while True:
            now = node_list[now].prev.number
            if now == a: break
            pos += 1
            Result.append(now)
            if now < Result[min_pos]: min_pos = pos
        print(" ".join(map(str, Result[min_pos:] + Result[:min_pos])))