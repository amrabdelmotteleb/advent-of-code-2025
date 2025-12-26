import math

# Input data
with open(r'input.txt', 'r') as f:
    data = f.read()
    ranges, ids = data.split('\n\n')
    ranges, ids = ranges.split('\n'), ids.split('\n')
    ids = [int(id_) for id_ in ids]
    ranges = [
        (int(range_.split('-')[0]), int(range_.split('-')[1])) for range_ in ranges
    ]

# P1
# ID is in any range -> fresh, spoiled o.w
ans = 0
for id_ in ids:
    for left, right in ranges:
        if left <= id_ <= right:
            ans += 1
            break


# P2
# Find all the possible fresh ingredients based on the list of ranges.
# Ranges can intersect -> need to identify the list of non-intersecting ranges -> count the total
# number of possible fresh ingredients.
ranges.sort(key=lambda range_: range_[0])

distinct_ranges = []
cur_l, cur_r = ranges[0]
for l, r in ranges:
    # Intersect
    if l <= cur_r:
        cur_r = max(cur_r, r)
    # Do not intersect
    else:
        distinct_ranges.append((cur_l, cur_r))
        cur_l, cur_r = l, r

distinct_ranges.append((cur_l, cur_r))

ans = 0
for l, r in distinct_ranges:
    ans += r - l + 1












