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

S_init = input()
N = int(input())

command = []
S_value = []

for _ in range(N):
    line = input().split()
    cmd = int(line[0])
    command.append(cmd)
    if cmd == 1 or cmd == 2:
        S_value.append(line[1])
    else:
        S_value.append("")

cur = Node(S_init)

for i in range(N):
    if command[i] == 1:
        new_node = Node(S_value[i])
        insert_prev(cur, new_node)
    if command[i] == 2:
        new_node = Node(S_value[i])
        insert_next(cur, new_node)
    if command[i] == 3: cur = cur.prev if cur.prev is not None else cur
    if command[i] == 4: cur = cur.next if cur.next is not None else cur
    print(cur.prev.data if cur.prev is not None else "(Null)", cur.data, cur.next.data if cur.next is not None else "(Null)")