with open('/Users/gracie/Desktop/COMP/COMP 232/extra credit/day4/input.txt', 'r') as f:
    lines = [line.strip() for line in f]

# Part 1
rows = len(lines)
cols = len(lines[0])

accessible = 0

neighbors = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),          (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]

r = 0
while r < rows:
    c = 0
    while c < cols:
        if lines[r][c] == "@":
            count_adj = 0

            i = 0
            while i < len(neighbors):
                dr, dc = neighbors[i]
                nr = r + dr
                nc = c + dc

                valid_row = (0 <= nr < rows)
                valid_col = (0 <= nc < cols)

                if valid_row and valid_col:
                    if lines[nr][nc] == "@":
                        count_adj = count_adj + 1

                i = i + 1

            if count_adj < 4:
                accessible = accessible + 1
        c = c + 1
    r = r + 1

print(accessible)

# Part 2
current_grid = []
r = 0
while r < rows:
    row_list = []
    c = 0
    while c < cols:
        row_list.append(lines[r][c])
        c = c + 1
    current_grid.append(row_list)
    r = r + 1

total_removed = 0

while True:
    removable_positions = []

    r = 0
    while r < rows:
        c = 0
        while c < cols:
            if current_grid[r][c] == '@':
                neighbor_count = 0

                dr = -1
                while dr <= 1:
                    dc = -1
                    while dc <= 1:
                        if not (dr == 0 and dc == 0):
                            nr = r + dr
                            nc = c + dc
                            if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
                                if current_grid[nr][nc] == '@':
                                    neighbor_count = neighbor_count + 1
                        dc = dc + 1
                    dr = dr + 1

                if neighbor_count < 4:
                    removable_positions.append((r, c))
            c = c + 1
        r = r + 1

    if len(removable_positions) == 0:
        break

    i = 0
    while i < len(removable_positions):
        rr, cc = removable_positions[i]
        current_grid[rr][cc] = '.'
        i = i + 1

    total_removed = total_removed + len(removable_positions)

print(total_removed)