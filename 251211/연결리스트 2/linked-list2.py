class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def insert_next(u, singleton):
    singleton.prev = u
    singleton.next = u.next
    singleton.prev.next = singleton
    if singleton.next is not None: singleton.next.prev = singleton

def insert_prev(u, singleton):
    singleton.prev = u.prev
    singleton.next = u
    if singleton.prev is not None: singleton.prev.next = singleton
    singleton.next.prev = singleton

def pop(u):
    if u.prev is not None: u.prev.next = u.next
    if u.next is not None: u.next.prev = u.prev
    u.prev = u.next = None

N = int(input())
Q = int(input())

type_arr = []
i_arr = []
j_arr = []

for _ in range(Q):
    query = list(map(int, input().split()))
    type_arr.append(query[0])
    i_arr.append(query[1])
    if query[0] in [2, 3]:
        j_arr.append(query[2])
    else:
        j_arr.append(0)

NodeList = [0]
for i in range(1, N + 1): NodeList.append(Node(i))

for i in range(Q):
    if type_arr[i] == 1: pop(NodeList[i_arr[i]])
    if type_arr[i] == 2: insert_prev(NodeList[i_arr[i]], NodeList[j_arr[i]])
    if type_arr[i] == 3: insert_next(NodeList[i_arr[i]], NodeList[j_arr[i]])
    if type_arr[i] == 4: print(NodeList[i_arr[i]].prev.data if NodeList[i_arr[i]].prev is not None else 0, NodeList[i_arr[i]].next.data if NodeList[i_arr[i]].next is not None else 0)

for i in range(1, N + 1): print(NodeList[i].next.data if NodeList[i].next is not None else 0, end = " ")