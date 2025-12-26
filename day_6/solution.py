from functools import reduce
import operator

# Data input
with open('input.txt', 'r') as f:
    lines = [line.strip().split(' ') for line in f]
    lines = [[entry for entry in line if entry != ''] for line in lines]
    # Ensure number of elements align after processing
    assert [len(line) for line in lines] == [len(lines[0])] * len(lines)
    digits, operations = lines[:4], lines[4]

op_map = {
    '+': operator.add,
    '*': operator.mul
}

# P1
digits_int = [[int(digit) for digit in line] for line in digits]
ans = 0
for op, values in zip(operations, zip(*digits_int)):
    ans += reduce(op_map[op], values)


# P2:
# Annoying part about this part is the alignment of the different numbers, as it is not consistent.
# Instead of identifying digits horizontally like we did in P1, we will be treating each line as a string,
# and moving through them to identify the numbers vertically.
with open('input.txt', 'r') as f:
    data = [line for line in f]
    operations, digits = data[4], data[:4]

iters = max([len(line) for line in data])
i = 0
ans = 0
while i < iters:
    if operations[i] in op_map:
        op = operations[i]
        values = []

        valid = True
        while valid:
            cur_val = ''
            for row in digits:
                if i < len(row):
                    row_char = row[i]
                    if row_char.isdigit():
                        cur_val += row_char

            if cur_val.isdigit():
                values.append(int(cur_val))

            else:
                valid = False

            i += 1

        ans += reduce(op_map[op], values)

    else:
        i += 1
















