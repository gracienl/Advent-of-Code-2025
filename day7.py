with open('/Users/gracie/Desktop/COMP/COMP 232/extra credit/day7/input.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f]

rows = len(lines)
cols = len(lines[0])

# Find S
start_r = -1
start_c = -1

r = 0
while r < rows:
    c = 0
    while c < cols:
        if lines[r][c] == 'S':
            start_r = r
            start_c = c
        c = c + 1
    r = r + 1

# Part 1: count splits

active = set()
active.add((start_r, start_c))

split_count = 0

while len(active) > 0:
    dest = set()

    for pos in active:
        r = pos[0]
        c = pos[1]
        nr = r + 1
        if nr < rows:
            dest.add((nr, c))

    new_active = set()

    for pos in dest:
        nr = pos[0]
        nc = pos[1]
        ch = lines[nr][nc]

        if ch == '.' or ch == 'S':
            new_active.add((nr, nc))
        elif ch == '^':
            split_count = split_count + 1

            lc = nc - 1
            if lc >= 0:
                new_active.add((nr, lc))

            rc = nc + 1
            if rc < cols:
                new_active.add((nr, rc))

    active = new_active

print("Part 1:", split_count)

# Part 2: count all timelines

timelines = 0

if start_r == rows - 1:
    timelines = 1
else:
    counts = [0] * cols
    counts[start_c] = 1
    current_row = start_r + 1

    while current_row < rows:
        next_counts = [0] * cols

        c = 0
        while c < cols:
            count_here = counts[c]

            if count_here > 0:
                ch = lines[current_row][c]

                if ch == '^':
                    left_col = c - 1
                    right_col = c + 1

                    # Left branch
                    if left_col >= 0:
                        if current_row == rows - 1:
                            timelines = timelines + count_here
                        else:
                            next_counts[left_col] = next_counts[left_col] + count_here
                    else:
                        timelines = timelines + count_here

                    # Right branch
                    if right_col < cols:
                        if current_row == rows - 1:
                            timelines = timelines + count_here
                        else:
                            next_counts[right_col] = next_counts[right_col] + count_here
                    else:
                        timelines = timelines + count_here

                else:
                    # Straight down
                    if current_row == rows - 1:
                        timelines = timelines + count_here
                    else:
                        next_counts[c] = next_counts[c] + count_here

            c = c + 1

        counts = next_counts
        current_row = current_row + 1

print("Part 2:", timelines)
