# first input is # chocs, next inputs are hm in jar, and jar capactiy

import sys
infile = sys.stdin
try:
    tokens = infile.readline().rstrip().split()
    chocolates = int(tokens[0])
except:
    print("Give me a number of chocolates.")
    quit()

# Initialize
jars = 0
count = 0
level = 0
capacity = 0

for l in infile:
    jars +=1
    tokens = l.rstrip().split()

    try:
        level = int(tokens[0])
        capactiy = int(tokens[1])
    except:
        # print("level is {}, capacity is {}".format(level,capactiy))
        print("ERROR - bad input on line{}, with tokens {}".format(jars,tokens))
        continue
    if capactiy - level >= chocolates:
        count += 1
print(count)
