with open('/Users/gracie/Desktop/COMP/COMP 232/extra credit/day6/input.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f]

width = max(len(line) for line in lines)
i = 0
while i < len(lines):
    if len(lines[i]) < width:
        lines[i] = lines[i].ljust(width)
    i = i + 1

rows = len(lines)
ops_line = lines[rows - 1]      # last row = operators
data_lines = lines[:rows - 1]   # rows above = digits

seps = [-1]
c = 0
while c < width:
    r = 0
    all_space = True
    while r < rows:
        if lines[r][c] != ' ':
            all_space = False
        r = r + 1
    if all_space:
        seps.append(c)
    c = c + 1
seps.append(width)

# Part 1

grand_total = 0

i = 0
while i < len(seps) - 1:
    left = seps[i]
    right = seps[i + 1]

    if right - left > 1:
        op = None
        c = left + 1
        while c < right:
            ch = ops_line[c]
            if ch == '+' or ch == '*':
                op = ch
            c = c + 1

        nums = []
        r = 0
        while r < len(data_lines):
            field = data_lines[r][left + 1:right]
            field_stripped = field.strip()
            if field_stripped != '':
                nums.append(int(field_stripped))
            r = r + 1

        if op == '+':
            result = 0
            j = 0
            while j < len(nums):
                result = result + nums[j]
                j = j + 1
        else:  # op == '*'
            result = 1
            j = 0
            while j < len(nums):
                result = result * nums[j]
                j = j + 1

        grand_total = grand_total + result

    i = i + 1

print("Part 1:", grand_total)

# Part 2

grand_total_2 = 0

i = 0
while i < len(seps) - 1:
    left = seps[i]
    right = seps[i + 1]

    if right - left > 1:
        op = None
        c = left + 1
        while c < right:
            ch = ops_line[c]
            if ch == '+' or ch == '*':
                op = ch
            c = c + 1

        nums = []

        col = right - 1
        while col > left:
            digits = ""
            r = 0
            while r < len(data_lines):
                ch = data_lines[r][col]
                if ch != ' ':
                    digits = digits + ch
                r = r + 1

            if digits != "":
                nums.append(int(digits))

            col = col - 1

        if op == '+':
            result = 0
            j = 0
            while j < len(nums):
                result = result + nums[j]
                j = j + 1
        else:  # op == '*'
            result = 1
            j = 0
            while j < len(nums):
                result = result * nums[j]
                j = j + 1

        grand_total_2 = grand_total_2 + result

    i = i + 1

print("Part 2:", grand_total_2)
