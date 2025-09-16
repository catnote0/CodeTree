N, G = map(int, input().split())

group_list = []
group_size = []

for _ in range(G):
    nums = list(map(int, input().split()))
    group_size.append(nums[0])
    group_list.append(set(nums[1:]))

member_group = [0]

for _ in range(N): member_group.append(set())

for i, group in enumerate(group_list):
    for m in group: member_group[m].add(i)

Count = 1
invitated_queue = [1]
invitated_set = set([1])

while invitated_queue:
    now_invitated = invitated_queue[0]
    for g in member_group[now_invitated]:
        group_list[g].remove(now_invitated)
        if len(group_list[g]) == 1:
            last_member = list(group_list[g])[0]
            if last_member not in invitated_set:
                invitated_queue.append(last_member)
                invitated_set.add(last_member)
                Count += 1
    del invitated_queue[0]

print(Count)