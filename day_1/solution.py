# Read input
with open('input.txt', 'r') as f:
    inputs = f.read()
    inputs = inputs.split('\n')
    directions = [inputs[i][0] for i in range(len(inputs))]
    moves = [int(inputs[i][1:]) for i in range(len(inputs))]

# P1
# 0 -> 99, if you reach 0 and move left, you go to 99, if you reach 99 and move right, you go to 0
# Count the number of times you visit 0 

direction_dict = {'L': -1, 'R': 1}
# Start at 50 
cur = 50 
ans = 0
for direction, move in zip(directions, moves):
    cur += direction_dict[direction] * move
    cur %= 100

    if cur == 0:
        ans += 1 

    
# P2 
# Need to count the number of times we passed through 0, not just the times the dial 
# landed on 0. 
ans = 0
cur = 50
for direction, move in zip(directions, moves):
    for _ in range(move):
        if direction == 'L':
            cur = (cur - 1) % 100
        else:
            cur = (cur + 1) % 100 
        
        if cur == 0:
            ans += 1

    # Negative side (slightly more tricky)