with open("/Users/gracie/Desktop/COMP/COMP 232/extra credit/day9/input.txt", "r") as f:
    points = [tuple(map(int, line.split(","))) for line in f if line.strip() != ""]

n = len(points)

# Part 1
max_area_part1 = 0
for i in range(n):
    x1, y1 = points[i]
    for j in range(i + 1, n):
        x2, y2 = points[j]
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
        if area > max_area_part1:
            max_area_part1 = area

print("Part 1:", max_area_part1)

# Part 2
edges = []
for i in range(n):
    x1, y1 = points[i]
    x2, y2 = points[(i + 1) % n]

    if x1 == x2:  # vertical
        if y1 <= y2:
            edges.append((x1, x2, y1, y2))
        else:
            edges.append((x1, x2, y2, y1))
    else:  # horizontal
        if x1 <= x2:
            edges.append((x1, x2, y1, y2))
        else:
            edges.append((x2, x1, y1, y2))

max_area_part2 = 0

for i in range(n):
    x1, y1 = points[i]
    for j in range(i + 1, n):
        x2, y2 = points[j]

        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

        if area > max_area_part2:

            xa = min(x1, x2)
            xb = max(x1, x2)
            ya = min(y1, y2)
            yb = max(y1, y2)

            valid = True

            for ex1, ex2, ey1, ey2 in edges:
                if ex2 > xa and ex1 < xb and ey2 > ya and ey1 < yb:
                    valid = False
                    break

            if valid:
                max_area_part2 = area

print("Part 2:", max_area_part2)
