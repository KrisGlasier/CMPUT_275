Lvls = input().strip().split()

def CheckRise(Elevation, i=None, memo=None):
    if memo is None:
        memo=[]
    if i is None:
        i=0
    memo.append(0)
    j = i+1
    k = i
    if j < len(Elevation)-2 and k < len(Elevation)-1:
        while Elevation[j] > Elevation[k]:
            memo[-1] += 1
            j+= 1
            k += 1
    if i < len(Elevation)-1 :
        return CheckRise(Elevation, i+1, memo)
    if i == len(Elevation)-1:
        return [str(n) for n in memo]


x = CheckRise(Lvls)
print(" ".join(x))
