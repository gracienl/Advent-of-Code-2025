data = []
with open('/Users/gracie/Desktop/COMP/COMP 232/extra credit/input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        direction = line[0].strip()
        distance = int(line[1:].strip())
        data.append((direction, distance))

pointer = 50
count_exact_0 = 0
# Part 1
for direction, distance in data:
    if direction == 'L':
        pointer = (pointer - distance) % 100
    else:
        pointer = (pointer + distance) % 100
    if pointer == 0:
        count_exact_0 += 1
print(count_exact_0)
# Part 2
pointer = 50
count_cross_0 = 0
for direction, distance in data:
    if direction == 'L':
        for i in range(distance):
            pointer = (pointer - 1) % 100
            if pointer == 0:
                count_cross_0 += 1
    else:
        for i in range(distance):
            pointer = (pointer + 1) % 100
            if pointer == 0:
                count_cross_0 += 1
print(count_cross_0)
