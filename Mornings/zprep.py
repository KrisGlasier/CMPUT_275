# Add your code here
L = input()
line = ""
# strip all non alpha
for i in L:
    if i.isalpha():
        line += i

# initialize z array. First element is always len of string
z = [str(len(line))]
index = 0


# counts the number of characters equal to the beginning of string
def isCoefficient(string, i):
    counter = 0
    for j in range(len(string)):
        if i >= len(string):
            return str(counter)
        if string[j] == string[i]:
            counter += 1
            i += 1
        else:
            return str(counter)


# runs through each possibility
for a in range(1, len(line)):
    z.append(isCoefficient(line, a))
# prints
print(" ".join(z))
