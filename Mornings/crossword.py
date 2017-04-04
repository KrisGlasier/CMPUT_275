import sys # Put your code here
n = input().strip().split()
n = [int(n[0]), int(n[1])]
words = []
for line in sys.stdin:
    words.append(line.strip())

incomplete = words[n[0]:]
words = sorted(words[:(n[0])])
Result = []

for IncomWord in incomplete:
    length = len(IncomWord)
    Result.append([])
    for Word in words:
        if len(Word) != length:
            continue
        possible = True
        for pos in range(length):
            if IncomWord[pos] == Word[pos]:
                continue
            elif IncomWord[pos] == "?":
                continue
            else:
                possible = False
                break
        if possible == True:
            Result[-1].append(Word)

for l in Result:
    print(" ".join(l))
