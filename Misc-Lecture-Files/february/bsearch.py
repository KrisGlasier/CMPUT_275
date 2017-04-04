def bsearch(l,x,low = None, high = None):
    if len(l) == 0:
        return False
    # We are looking at the slice l[Low:high]

    if low == None:
        low = 0
    if high == None:
        high = len(l)

    while low < high:
        mid = (low + high) // 2
        if x == l[mid]:
            return True
        if x < l[mid]:
            high = mid
        else:
            low = mid + 1
    return False

def bsearch_test(n):
    import doctest
    doc.testmod()


import random
l = sorted([ random.randint(0,10) for i in range(10)])
x = bsearch(l,5)
print(x)
