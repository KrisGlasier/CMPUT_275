import sys
word = ''
printing = 0
inpunchcard = False

for line in sys.stdin:
    if line:
        if line[0] == '|':
            inpunchcard = True
            lines = line.strip()
            lines = lines[2:16:2].replace("o","1").replace(" ","0")
            lines = int(lines,base=2)
            word += chr(lines)
        if line[0] == "-" and inpunchcard:
            inpunchcard = False
            print(word)
            word = ''
    else: continue
