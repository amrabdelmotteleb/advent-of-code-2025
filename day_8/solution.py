from collections import defaultdict

with open('input.txt', 'r') as f:
    data = f.read()
    coordinates = [coord.split(',') for coord in data.split('\n')]
    coordinates = [tuple(int(entry) for entry in coord) for coord in coordinates]

# Setup (Union Find algos)
def find(x):
    if x == UF[x]:
        return x

    UF[x] = find(UF[x])
    return UF[x]

def union(x, y):
    UF[find(x)] = find(y)

# P1
dists = []
for i in range(len(coordinates)):
    for j in range(i):
        x1, y1, z1 = coordinates[i]
        x2, y2, z2 = coordinates[j]
        dist = (x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2
        dists.append((dist, i, j))

# Union Find dict
UF = {i: i for i in range(len(coordinates))}

dists = sorted(dists, key=lambda x: x[0])
for dist, i, j in dists[:1000]:
    union(i, j)

components_sizes = defaultdict(int)
for i in range(len(coordinates)):
    components_sizes[find(i)] += 1

sorted_sizes = sorted(components_sizes.values())
ans = sorted_sizes[-3] * sorted_sizes[-2] * sorted_sizes[-1]

# P2
UF = {i: i for i in range(len(coordinates))}

found = False
for dist, i, j in dists:
    if found:
        break

    # Add link
    union(i, j)

    # Update UF, check if the root for every coord is the same
    heads = set()
    for z in UF:
        cur_head = find(z)
        heads.add(cur_head)

    if len(heads) == 1: # 1 connected component
        found = True
        ans = coordinates[i][0] * coordinates[j][0]

# Another more efficient solution is to count the number of new connections created as you go through 'dists'!
UF = {i: i for i in range(len(coordinates))}

connections = 0
for dist, i, j in dists:
    if find(i) != find(j):
        connections += 1

    # Add link
    union(i, j)

    if connections == len(coordinates) - 1:
        ans = coordinates[i][0] * coordinates[j][0]
        break
