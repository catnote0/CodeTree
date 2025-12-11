import heapq

N = int(input())
commands = []

queue = []

for _ in range(N):
    line = input().split()
    if line[0] == "push":
        commands.append((line[0], int(line[1])))
    else:
        commands.append((line[0],))

# Please write your code here.

for line in commands:
    if line[0] == "push": heapq.heappush(queue, -line[1])
    if line[0] == "size": print(len(queue))
    if line[0] == "empty": print(1 if not queue else 0)
    if line[0] == "pop": print(-heapq.heappop(queue))
    if line[0] == "top": print(-queue[0])