from collections import deque

# Data input
with open('input.txt', 'r') as f:
    data = f.read()
    data = data.split('\n')
    data = [[char for char in line] for line in data]

# Setup
start = (0, (len(data[0]) - 1) // 2)
Q = deque([start])
R = len(data)
C = len(data[0])


# P1
ans = 0
seen = set()
while Q:
    r, c = Q.popleft()
    if r >= R - 1 or c >= C - 1 or (r, c) in seen:
        continue

    nr = r + 1
    if data[nr][c] == '^':
        nr1, nc1 = nr, c - 1
        nr2, nc2 = nr, c + 1
        Q.append((nr1, nc1))
        Q.append((nr2, nc2))
        ans += 1

    else:
        Q.append((nr, c))

    seen.add((r, c))

# P2
# state: (r, c)
# memo[state] = number of possible timelines from that point to the bottom
# want to find memo[starting_point]

def f_rec(r, c):
    # Reached the bottom
    if r == R - 1:
        return 1

    if (r, c) in memo:
        return memo[(r, c)]

    if data[r][c] == '^':
        left = f_rec(r, c-1) if c > 0 else 0
        right = f_rec(r, c+1) if c < C - 1 else 0
        res = left + right

    else:
        res = f_rec(r+1, c)

    memo[(r, c)] = res
    return res


ans = 0
memo = {}
ans += f_rec(*start)





