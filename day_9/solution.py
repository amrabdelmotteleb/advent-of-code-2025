import math
from shapely.geometry import Polygon, box
from shapely.plotting import plot_polygon
import matplotlib.pyplot as plt

with open('input.txt', 'r') as f:
    data = f.read().split('\n')
    red_tiles = [tuple(int(entry) for entry in row.split(',')) for row in data]

# P1
# Note that the indexing here (i, j), i -> column index, j -> row index
# Simplest solution -> Brute force

ans = -math.inf
for i in range(len(red_tiles)):
    for j in range(i):
        i1, j1 = red_tiles[i]
        i2, j2 = red_tiles[j]

        s1 = abs(i1 - i2) + 1
        s2 = abs(j1 - j2) + 1
        cur_area = s1 * s2
        if cur_area > ans:
            ans = cur_area


# P2
# Simplest solution I can think of is by using shapely
polygon = Polygon(red_tiles)

ans = -math.inf
for i in range(len(red_tiles)):
    for j in range(i + 1, len(red_tiles)):
        i1, j1 = red_tiles[i]
        i2, j2 = red_tiles[j]

        rectangle = box(min(i1, i2), min(j1, j2), max(i1, i2), max(j1, j2))

        if polygon.covers(rectangle):
            area = (abs(i2 - i1) + 1) * (abs(j2 - j1) + 1)
            if area > ans:
                ans = area

# Extra: Plot the polygon!
plot_polygon(polygon)
plt.plot(*zip(*red_tiles), 'ro-')  # Red dots connected by lines
plt.savefig('polygon_plot.png', dpi=300, bbox_inches='tight')  # Save it






