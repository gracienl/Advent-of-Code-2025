with open("/Users/gracie/Desktop/COMP/COMP 232/extra credit/day8/input.txt", "r") as f:
    lines = [line.strip() for line in f if line.strip() != ""]

points = []
i = 0
while i < len(lines):
    x_str, y_str, z_str = lines[i].split(",")
    x = int(x_str)
    y = int(y_str)
    z = int(z_str)
    points.append((x, y, z))
    i = i + 1

n = len(points)

edges = []
i = 0
while i < n:
    j = i + 1
    while j < n:
        x1, y1, z1 = points[i]
        x2, y2, z2 = points[j]

        dx = x1 - x2
        dy = y1 - y2
        dz = z1 - z2
        dist2 = dx * dx + dy * dy + dz * dz

        edges.append((dist2, i, j))
        j = j + 1
    i = i + 1

edges.sort(key=lambda e: e[0])

parent = []
size = []

i = 0
while i < n:
    parent.append(i)
    size.append(1)
    i = i + 1

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra = find(a)
    rb = find(b)
    if ra == rb:
        return
    if size[ra] < size[rb]:
        tmp = ra
        ra = rb
        rb = tmp
    parent[rb] = ra
    size[ra] = size[ra] + size[rb]

# Part 1
num_pairs_to_add = 1000
if num_pairs_to_add > len(edges):
    num_pairs_to_add = len(edges)

k = 0
while k < num_pairs_to_add:
    _, i, j = edges[k]
    union(i, j)
    k = k + 1

root_count = {}
i = 0
while i < n:
    r = find(i)
    if r in root_count:
        root_count[r] = root_count[r] + 1
    else:
        root_count[r] = 1
    i = i + 1

sizes = list(root_count.values())
sizes.sort(reverse=True)

if len(sizes) >= 3:
    answer_part1 = sizes[0] * sizes[1] * sizes[2]
elif len(sizes) == 2:
    answer_part1 = sizes[0] * sizes[1]
elif len(sizes) == 1:
    answer_part1 = sizes[0]
else:
    answer_part1 = 0

print(answer_part1)

# Part 2

parent = []
size = []

i = 0
while i < n:
    parent.append(i)
    size.append(1)
    i = i + 1

components = n
last_i = -1
last_j = -1

k = 0
while k < len(edges) and components > 1:
    _, i_idx, j_idx = edges[k]

    ri = find(i_idx)
    rj = find(j_idx)

    if ri != rj:
        if size[ri] < size[rj]:
            tmp = ri
            ri = rj
            rj = tmp
        parent[rj] = ri
        size[ri] = size[ri] + size[rj]

        components = components - 1
        last_i = i_idx
        last_j = j_idx

    k = k + 1

if last_i != -1:
    x1 = points[last_i][0]
    x2 = points[last_j][0]
    answer_part2 = x1 * x2
else:
    answer_part2 = 0

print(answer_part2)
