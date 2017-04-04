# read code->word map
n = int(input())
code2word = dict()

# read encoded sentence
for _ in range(n):
    line = input().strip().split()
    code2word[line[0]] = line[1]
binaryWord = input().strip()

# decode sentence
test = ""
trueString = []
for i in binaryWord:
    test += i
    if test in code2word:
        trueString.append(code2word[test])
        test = ""


print(" ".join(trueString))
