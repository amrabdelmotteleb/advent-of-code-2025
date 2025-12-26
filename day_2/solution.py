# Input data
with open('input.txt', 'r') as f:
    input = f.read()
    id_ranges = input.split(',')
    parsed = [tuple(map(int, id_range.split('-'))) for id_range in id_ranges]
    start, end = zip(*parsed)

# P1

# Sequence repeated twice -> only consider numbers made up of an even number of digits
ans = 0
for s, e in zip(start, end):
    str_s, str_e = str(s), str(e)

    if (len(str_s) % 2 == 1) and (len(str_e) % 2 == 1):
        # Note: Can be made it a bit more efficient by checking for cases where
        # only one of the starting/ending numbers is an odd number, by updating
        # the starting/ending number so that both the starting and ending numbers
        # are made up of an even number of digits.
        continue

    cur = s
    while cur <= e:
        str_cur = str(cur)
        len_cur = len(str_cur)
        if len_cur % 2 == 0:
            first_half, second_half = str_cur[:len_cur // 2], str_cur[len_cur // 2:]
            if first_half == second_half:
                ans += cur

        cur += 1


# P2

# Sequence repeated at least twice:
# - Even number: 121212 now would be invalid, need to account for this
# - Odd number: Only possibility is if the number has 1 digit that keeps getting repeated

def get_divisors(n):
    return [i for i in range(1, n) if n % i == 0]


ans = 0
for s, e in zip(start, end):
    cur = s
    while cur <= e:
        str_cur = str(cur)
        len_cur = len(str_cur)

        if len_cur > 1:
            divisors = get_divisors(len_cur)
            for div in divisors:
                rep = str_cur[:div] * (len_cur // div)
                if rep == str_cur:
                    ans += cur
                    # Ensure we add it only once to our ans
                    break

        cur += 1




