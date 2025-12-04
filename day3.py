with open('/Users/gracie/Desktop/COMP/COMP 232/extra credit/day3/input.txt', 'r') as file:
    banks = file.read().strip().splitlines()

#Part 1
total = 0

for bank in banks:
    best_for_bank = 0

    for i in range(len(bank)):
        for j in range(i + 1, len(bank)):
            first_digit = int(bank[i])
            second_digit = int(bank[j])
            value = first_digit * 10 + second_digit

            if value > best_for_bank:
                best_for_bank = value

    total += best_for_bank

print(total)

#Part 2
total = 0
for bank in banks:
    result = ""

    start = 0
    while len(result) < 12:
        remaining = 12 - len(result)

        end_limit = len(bank) - remaining

        best_digit = '0'
        best_pos = start

        for i in range(start, end_limit + 1):
            if bank[i] > best_digit:
                best_digit = bank[i]
                best_pos = i

        result += best_digit
        start = best_pos + 1
    total += int(result)

print(total)

