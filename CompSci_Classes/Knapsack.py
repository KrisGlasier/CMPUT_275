
values = [5,10,2,4,5]
sizes  = [10,7,3,4,1]

def knapsack(k, capacity, memo=None):
    ''' Calculates the max value that can be acheived suing the items 0...k
        whose values and sizes are in the identically named global variables
        (outch!) while meeting the constraint that the total size of the
        packed items <= Capacity.'''

    if memo is None:
        memo = dict()
    if (k,capacity) in memo:
        return memo[(k,capacity)]
    if k==0:
        ret =  0 if sizes[0] > capacity else values[0]
        memo[(k,capacity)] = ret
        return ret
    max_value = knapsack(k-1,capacity)
    if sizes[k] <= capacity:
        packing_value = values[k] + knapsack(k-1,capacity-sizes[k], memo)
        max_value = max(max_value,packing_value)
    memo[(k,capacity)] = max_value
    return max_value

print(knapsack(len(values)-1,10))
