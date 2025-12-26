# Input data
with open('input.txt', 'r') as f:
    data = f.read()
    grid = data.split('\n')

# Directions
directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1)
]

R = len(grid)
C = len(grid[0])

# P1
ans = 0
for r in range(R):
    for c in range(C):
        if grid[r][c] == "@":
            adj_tp_count = 0
            for cr, cc in directions:
                ur, uc = r + cr, c + cc
                if (0 <= ur < R) and (0 <= uc < C) and grid[ur][uc] == "@":
                    adj_tp_count += 1

                if adj_tp_count >= 4:
                    break

            if adj_tp_count < 4:
                ans += 1

# P2
ans = 0
# List version
grid = [[char for char in row] for row in grid]

while True:
    changes = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == "@":
                adj_tp_count = 0
                for cr, cc in directions:
                    ur, uc = r + cr, c + cc
                    if (0 <= ur < R) and (0 <= uc < C) and grid[ur][uc] == "@":
                        adj_tp_count += 1

                    if adj_tp_count >= 4:
                        break

                if adj_tp_count < 4:
                    changes += 1
                    grid[r][c] = "."

    if changes == 0:
        break

    else:
        ans += changes











