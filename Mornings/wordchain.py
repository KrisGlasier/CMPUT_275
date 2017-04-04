# add your solution here

import sys
infile = sys.stdin
Words = []
for l in infile:
    Words.append(l.rstrip())

LetterCount = {}
for w in Words:
    LetterCount.setdefault(w[0],0)
    LetterCount[w[0]] += 1

Low = min(LetterCount.values())

minLetters = [letter for letter,value in LetterCount.items() if value == Low]
minWords = [word for word in Words if word[0] in minLetters]

print(Low)
print(*minWords, sep='\n')
