import re
from scipy.optimize import linprog
import numpy as np

# P1
# Brute force solution. Feasible given that the number of buttons we have is not too big for every machine.
total_ans = 0
with open('input.txt', 'r') as f:
    for line in f:
        line = line.split()
        cur_buttons = line[1:-1]
        cur_goal = line[0]
        cur_goal = cur_goal[1:-1]

        # Represent lights as a number
        solution = 0
        for i, char in enumerate(cur_goal):
            if char == '#':
                solution += 2**i

        buttons_n = []
        for button in cur_buttons:
            nums = [int(x) for x in button[1:-1].split(',')]
            button_n = sum(2**x for x in nums)
            buttons_n.append(button_n)

        # Brute force
        ans = len(cur_buttons) # worst case scenario, click on each button once
        for scenario in range(2**len(cur_buttons)):
            num_presses = 0
            n = 0
            for i in range(len(cur_buttons)):
                # Check if the i-th bit is 1
                if ((scenario>>i) % 2) == 1:
                    # Press on button i
                    n ^= buttons_n[i]
                    num_presses += 1

            if n == solution:
                ans = min(ans, num_presses)

        total_ans += ans

# Another solution for this is solving Ax = b, where A is a matrix containing each button as a column.
# For each column c_i, c_ij = 1 if the jth light is turned on, 0 if not.
# b is the vector representing which lights are on (e.g. .##. -> [0, 1, 1, 0])
# Ax would then be x_1*c_1 + x_2*c_2 + ...
# Note that in this case, it would be on the field GF[2], where 1 + 1 = 0, since turning a light on
# twice in this part is equivalent to not having done anything.

# P2
# This is a bit more intuitive, where it can be solved by solving Ax = b, with the constraint that we want to minimize
# sum(x)
def create_equation_components(buttons, goal):
    """Creates A and b in the equation Ax = b we are trying to solve."""
    b = np.array(goal)

    col_len = len(b)
    cols = []
    for button in buttons:
        col = [0] * col_len
        for ind in button:
            col[ind] = 1

        cols.append(col)

    A = np.column_stack(cols)
    return A, b

def ilp_solver(A, b):
    """
    Solve using scipy's Integer Linear Programming.

    Minimize: sum(x_i)  (total button presses)
    Subject to: Ax = b  (achieve target joltages)
                x_i ≥ 0 (can't press negative times)
                x_i is an integer
    """
    n_buttons = A.shape[1]

    # Minimize sum of x_i
    c = np.ones(n_buttons)

    # Equality constraint (Ax = b)
    A_eq = A.astype(float)
    b_eq = b.astype(float)

    # Bounds: x_i >= 0
    bounds = [(0, None) for _ in range(n_buttons)]

    # Integer constraint
    integrality = np.ones(n_buttons, dtype=int)

    res = linprog(
        c=c,
        A_eq=A_eq,
        b_eq=b_eq,
        bounds=bounds,
        integrality=integrality,
        method='highs',
    )

    if res.success:
        # Round to avoid floating point errors (should already be integers)
        solution = np.round(res.x).astype(int)
        total_presses = int(np.sum(solution))
        return total_presses

    else:
        raise ValueError('Did not find a solution.')

total_ans = 0
with open('input.txt', 'r') as f:
    for line in f:
        line = line.split()
        cur_buttons = line[1:-1]
        cur_goal = line[-1]

        cur_buttons = [tuple(int(x) for x in button[1:-1].split(',')) for button in cur_buttons]
        cur_goal = tuple(x for x in cur_goal[1:-1].split(','))

        A, b = create_equation_components(buttons=cur_buttons, goal=cur_goal)
        total_ans += ilp_solver(A, b)
