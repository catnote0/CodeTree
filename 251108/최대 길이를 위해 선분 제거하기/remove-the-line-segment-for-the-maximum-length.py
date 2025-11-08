n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

single_length = [0] * n
length = 0

end_list = []
for i, line in enumerate(segments):
    end_list.append((line[0], i, 1))
    end_list.append((line[1], i, -1))

end_list.sort(key = lambda x:x[0])

line_set = set()
for i, (x, num, status) in enumerate(end_list):
    if len(line_set) == 1: single_length[next(iter(line_set))] += end_list[i][0] - end_list[i - 1][0]
    if len(line_set) > 0: length += end_list[i][0] - end_list[i - 1][0]
    if status == 1: line_set.add(num)
    if status == -1: line_set.remove(num)

print(length - min(single_length))