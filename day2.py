with open('/Users/gracie/Desktop/COMP/COMP 232/extra credit/day2/input.txt', 'r') as file:
    line = file.read().strip()
#Part 1
total = 0
ranges = line.split(',')
for r in ranges:
    start, end = r.split('-')
    start = int(start)
    end = int(end)

    for num in range(start, end + 1):
        num_str = str(num)
        length = len(num_str)
        if length % 2 == 0:
            half = length // 2
            first_half = num_str[:half]
            second_half = num_str[half:]
            if first_half == second_half:
                total += num
print(total)

#Part 2

total = 0
ranges = line.split(',')
for r in ranges:
    start, end = r.split('-')
    start = int(start)
    end = int(end)

    for num in range(start, end + 1):
        num_str = str(num)
        length = len(num_str)
        invalid = False

        for i in range(1, length//2 + 1):
            if length % i == 0:
                pattern = num_str[:i]
                repetitions = length // i
                if pattern * repetitions == num_str:
                    invalid = True
                    break
        if invalid:
            total += num
print(total)