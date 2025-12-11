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
queries = [tuple(map(int, input().split())) for _ in range(Q)]
a, b, c, d = zip(*queries)
a, b, c, d = list(a), list(b), list(c), list(d)

NodeList = [0]
for i in range(1, N + 1):
    NodeList.append(Node(i))
    if i > 1: insert_next(NodeList[i - 1], NodeList[i])

for i in range(Q):
    a_prev = NodeList[a[i]].prev
    b_next = NodeList[b[i]].next
    c_prev = NodeList[c[i]].prev
    d_next = NodeList[d[i]].next
    if c_prev is not None and c_prev.data == b[i]:
        NodeList[c[i]].prev = a_prev
        NodeList[d[i]].next = NodeList[a[i]]
        NodeList[a[i]].prev = NodeList[d[i]]
        NodeList[b[i]].next = d_next
        if a_prev is not None: a_prev.next = NodeList[c[i]]
        if d_next is not None: d_next.prev = NodeList[b[i]]
    elif a_prev is not None and a_prev.data == d[i]:
        NodeList[a[i]].prev = c_prev
        NodeList[b[i]].next = NodeList[c[i]]
        NodeList[c[i]].prev = NodeList[b[i]]
        NodeList[d[i]].next = b_next
        if c_prev is not None: c_prev.next = NodeList[a[i]]
        if b_next is not None: b_next.prev = NodeList[d[i]]
    else:
        NodeList[c[i]].prev = a_prev
        if a_prev is not None: a_prev.next = NodeList[c[i]]
        NodeList[d[i]].next = b_next
        if b_next is not None: b_next.prev = NodeList[d[i]]
        NodeList[a[i]].prev = c_prev
        if c_prev is not None: c_prev.next = NodeList[a[i]]
        NodeList[b[i]].next = d_next
        if d_next is not None: d_next.prev = NodeList[b[i]]

for i in range(1, N + 1):
    if NodeList[i].prev is None:
        curr = NodeList[i]
        while curr is not None:
            print(curr.data, end = " ")
            curr = curr.next
        exit(0)