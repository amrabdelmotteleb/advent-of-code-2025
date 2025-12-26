with open('input.txt', 'r') as f:
    input_str = f.read()

# P1
# Can only think of using a backtracking solution for this question, where we brute force our way
# into finding a possible answer.
# Calculate areas to fail early if the area of the grid is smaller than the area of the shapes they want us to fit.
sections = input_str.split('\n\n')
shapes, queries = sections[:-1], sections[-1].split('\n')

# Utils
def flip_shape(shape):
    return [(r, -c) for r, c in shape]


def rotate_shape(shape):
    """Rotate 90 degrees clockwise."""
    return [(c, -r) for r, c in shape]


def normalize_shape(shape):
    """Normalize shape to canonical form."""
    min_r = min(coord[0] for coord in shape)
    min_c = min(coord[1] for coord in shape)

    normalized_shape = [(r - min_r, c - min_c) for r, c in shape]
    return tuple(sorted(normalized_shape))

def get_orientations(shape):
    orientations = set()
    cur = shape
    for _ in range(2): # Flips
        for _ in range(4): # Rotations
            normalized = normalize_shape(cur)
            orientations.add(normalized)
            cur = rotate_shape(cur)
        cur = flip_shape(cur)

    return orientations


# Dictionary containing the list of variations for each shape we have
# Shape ID -> list of variations
# Each variation is represented as a list of the coordinates that make up the shape

shape_library = {}
shape_area = {}
# Parse shapes
for shape_id, shape in enumerate(shapes):
    shape = shape.split('\n')[1:]

    original_coords = []
    for r, row in enumerate(shape):
        for c, char in enumerate(row):
            if char == '#':
                original_coords.append((r, c))

    shape_area[shape_id] = len(original_coords)
    # Some variations might be symmetric to other ones
    orientations = get_orientations(original_coords)
    shape_library[shape_id] = orientations


queries_library = []
for query in queries:
    dimensions, num_shapes = query.split(':')
    W, H = dimensions.split('x')
    W, H = int(W), int(H)
    num_shapes = [int(x) for x in num_shapes.split()]
    cur = {'w': W, 'h': H, 'num_shapes': num_shapes}
    queries_library.append(cur)


ans = 0
for query in queries_library:
    W, H, num_shapes = query['w'], query['h'], query['num_shapes']
    all_pieces = []
    for shape_id, count in enumerate(num_shapes):
        if count > 0:
            shape_orientations = shape_library[shape_id]
            for _ in range(count):
                all_pieces.append(shape_orientations)

    # Early failure
    total_area = sum(shape_count * shape_area[i] for i, shape_count in enumerate(num_shapes))
    if total_area > W * H:
        continue

    # Backtracking sol
    grid = [[False] * W for _ in range(H)]

    def backtrack(idx):
        # Done
        if idx == len(all_pieces):
            return True

        current_variations = all_pieces[idx]

        for coords in current_variations:
            h = max(r for r, c in coords) + 1
            w = max(c for r, c in coords) + 1

            for r in range(H - h + 1):
                for c in range(W - w + 1):
                    fits = True

                    for dr, dc in coords:
                        if grid[r + dr][c + dc]:
                            fits = False
                            break

                    if fits:
                        for dr, dc in coords:
                            grid[r + dr][c + dc] = True

                        if backtrack(idx + 1):
                            return True

                        # Backtracking step
                        for dr, dc in coords:
                            grid[r + dr][c + dc] = False

        return False

    if backtrack(0):
        ans += 1
