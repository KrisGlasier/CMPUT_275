num_matches = int(input())

# Denotes the current winners- first two elements are the winners
# in a round, Alice and Bob respectively, and the last two are winners for
# the matches, overall.
win = [0,0,0,0]

for i in range(num_matches):
    pass
    win[0],win[1] = [0,0] # Resets the rounds counter
    rounds = input().split()
    # Couldn't think of a more elegant way to do this. Help?
    for e in rounds:
        if e[0] == 'R':
            if e[1] == 'P':
                win[1] += 1
            elif e[1] == 'S':
                win[0] += 1
        elif e[0] == 'P':
            if e[1] == 'S':
                win[1] += 1
            elif e[1] == 'R':
                win[0] += 1
        elif e[0] == 'S':
            if e[1] == 'R':
                win[1] += 1
            elif e[1] == 'P':
                win[0] += 1
    if win[0] > win[1]: win[2] += 1
    elif win[0] < win[1]: win[3] += 1

# Equals to in the case that the first person to said number would
# win in the case of a tie.
if win[2] >= win[3]: print("Alice",win[2])
elif win[2] <= win[3]: print("Bob",win[3])
