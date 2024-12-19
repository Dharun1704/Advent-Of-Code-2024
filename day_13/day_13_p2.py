with open("./day_13/day_13.txt") as fin:
    slots = fin.read().strip().split('\n\n')
total = 0
part2_addition = 10000000000000

for slot in slots:
    lines = slot.split('\n')
    all_numbers = []
    for line in lines:
        components = line.split(',') 
        numbers_in_line = []
        for component in components:
            numeric_value = int(''.join([char for char in component if char.isnumeric()]))
            numbers_in_line.append(numeric_value)
        all_numbers.extend(numbers_in_line)

    x1, y1, x2, y2, x, y = all_numbers 
    x, y = x + part2_addition, y + part2_addition
    d = (x1 * y2 - x2 * y1)
    i = ((y2 * x - x2 * y) / d)
    j = ((-y1 * x + x1 * y) / d)
    if (int(i)) * x1 + (int(j)) * x2 == x and (int(i)) * y1 + (int(j)) * y2 == y:
        total += (int(i)) * 3 + (int(j))

print(total)

