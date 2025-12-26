with open('input.txt', 'r') as f:
    data = f.read()
    data = data.split('\n')
    keys = [line.split(':')[0] for line in data]
    values = [line.split(':')[1] for line in data]
    values = [line.split() for line in values]
    mapping = {k: vs for k, vs in zip(keys, values)}

# P1
# DFS + Memoization
p1_num_routes = {}
def p1_dfs(start, seen):
    if start == 'out':
        return 1

    # Cycle detection
    if start in seen:
        return 0

    if start in p1_num_routes:
        return p1_num_routes[start]

    routes_count = 0

    seen.add(start)
    for nxt in mapping[start]:
        routes_count += p1_dfs(nxt, seen)
    seen.remove(start)

    p1_num_routes[start] = routes_count
    return routes_count

p1_ans = p1_dfs('you', set())

# P2
# Keep track of the key + whether the path explored has 'dac' + whether the path explored has 'fft'
p2_num_routes = {}
def p2_dfs(start, seen_dac, seen_fft, seen):
    if start == 'out':
        return 1 if (seen_dac and seen_fft) else 0

    # Circular
    if start in seen:
        return 0

    state = (start, seen_dac, seen_fft)
    if state in p2_num_routes:
        return p2_num_routes[state]


    # Update state
    new_dac = seen_dac or (start == 'dac')
    new_fft = seen_fft or (start == 'fft')

    routes_count = 0
    seen.add(start)
    for nxt in mapping[start]:
        routes_count += p2_dfs(nxt, new_dac, new_fft, seen)
    seen.remove(start)

    p2_num_routes[state] = routes_count
    return routes_count

p2_ans = p2_dfs('svr', False, False, set())
