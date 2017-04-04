# add you code here
import sys
x = []
for i in sys.stdin:
    x.append(i.strip().split())
T = int(x[0][0])
pos = []
cars = x[1]
for i in range(len(cars)):
    cars[i] = int(cars[i])
    pos.append(i)

for i in range(len(cars)):
    pos[i] = pos[i] + cars[i]*T

passed = 0
for j in range(len(pos)-1):
    for k in range(j, len(pos)):
        if pos[j] > pos[k]:
            passed = passed + 1
print(passed)
