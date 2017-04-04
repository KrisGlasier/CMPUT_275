import sys
sys.setrecursionlimit(2500)

def fib(i,memo=None):
    """ calcualte the i-th Fibonacci number where i > 0
        Time complexity is O(i^2)
        Space complexity is S(i^2)
        fib(i) needs about i bits"""
    if memo is None:
        memo=dict()
    if i in memo:
        return memo[i]
    if i<=1:
        memo[i] = i
        return i
    n=fib(i-1,memo) + fib(i-2,memo)
    memo[i] = n
    return n

x = int(input("What i-th Fibonacci number would you like? "))
print(fib(x))
