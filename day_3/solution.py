# Input data
with open('input.txt', 'r') as f:
    data = f.read()
    banks = data.split('\n')

# P1
ans = 0
for bank in banks:
    first = second = None
    for i, num in enumerate(bank):
        num = int(num)
        if first is None:
            first = num
            continue

        if num > first and i < len(bank) - 1:
            first, second = num, None
            continue

        if second is None or num > second:
            second = num
            continue

    res = int(str(first) + str(second))
    ans += res

# P2
# State: (i, used)
# i: bank index
# used: number of used digits (out of 12)
def f_dp(bank, i, used):
    if i == len(bank) and used == 12:
        return 0

    # Out of bounds
    if i == len(bank):
        return -10**100

    state = (i, used)
    if state in dp:
        return dp[state]

    cur = f_dp(bank, i+1, used)
    if used < 12:
        cur = max(
            cur, # do not include
            10**(11-used)*int(bank[i]) + f_dp(bank, i+1, used+1) # include
    )

    dp[state] = cur
    return cur


ans = 0
for bank in banks:
    dp = {}
    ans += f_dp(bank, 0, 0)





