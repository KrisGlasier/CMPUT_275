debug = False

def bsearch_side(l, k, find_high_side=False, low=None, high=None):
    """
    Binary search a list l for low or high side boundary of a k-region
    of key k.

    Inputs:
    l is a list, possibly empty, possibly containing duplicates, that is
    ordered in non-decreasing order.

    k is the value to search for in l.  There may be 0 or more occurrences
    of k in l.  The k-region in l is the range of positions in l where
    a sequences of k's would appear.  For example, in
        l = [0, 2, 4, 4, 4, 6, 7]
    the k-region for
        k = 4 is range(2, 5)
        k = 6 is range(5, 6)
        k = 1 is range(1, 1)

    find_high_side - the side of the k-region to identify, if False, find
        the low (left hand) side, if True find the high (right hand) side.

    low, high if present indicate the slice l[low:high] of l to search,
    ignoring the other parts of l, which might contain occurences of k.
    Default values of low is 0, high = len(l)

    Outputs:

    Returns position pos in range(low, high) such that

    if ! find_high_side:
        pos is such that l[pos] is the largest value < k.
        That is, inserting k before pos will increase the existing
        k-region of k's on the left by one more k.

    if find_high_side:
        pos is such that l[pos] is the smallest value > k.
        That is, inserting k before pos will increase the existing
        k-region of k's on the right by one more k.

    Note that if k is not present in l, then the same position is returned
    for both low and high sides.

    Complexity: O( log(high-low+1) )

    Doc tests:

    >>> bsearch_side( [ ], 42)
    0
    >>> bsearch_side( [ ], 42, find_high_side=True)
    0
    >>> u = [9, 9, 9, 9]
    >>> bsearch_side(u, 9)
    0
    >>> bsearch_side(u, 9, find_high_side=True)
    4
    >>> bsearch_side(u, -1)
    0
    >>> bsearch_side(u, -1, find_high_side=True)
    0
    >>> bsearch_side(u, 11)
    4
    >>> bsearch_side(u, 11, find_high_side=True)
    4
    >>> s = [2, 2, 3, 5, 6, 7, 9, 9, 9, 10, 11, 11]
    >>> bsearch_side(s, 9)
    6
    >>> bsearch_side(s, 9, find_high_side=True)
    9
    >>> bsearch_side(s, -1)
    0
    >>> bsearch_side(s, -1, find_high_side=True)
    0
    >>> bsearch_side(s, 13)
    12
    >>> bsearch_side(s, 13, find_high_side=True)
    12
    >>> bsearch_side(s, 5)
    3
    >>> bsearch_side(s, 5, find_high_side=True)
    4
    """

    if low is None:
        low = 0
    else:
        low = low

    if high is None:
        high = len(l)
    else:
        high = high

    debug and print(l)
    debug and print(list(range(0,len(l))))

    # Invariant:
    # If k is in l, then it must be in the slice l[low:high]
    # So if low = high then k is not in l

    while low < high:
        # Split the list
        mid = (low + high) // 2

        debug and print(
            "k {} [{}, {}:{}, {}]" .format(k, low, mid, l[mid], high))

        if not find_high_side:
            # Find the low side position
            # HINT: Do a normal binary search, but pretend that search key
            # is k-epsilon, i.e. the largest value < k.  How does k-epsilon
            # compare to l[mid], especially when l[mid] = k?
            # YOUR CODE GOES HERE
            if k <= l[mid]:
                high = mid
            else:
                low = mid + 1
        else:
            # Find the high side position
            # Do a normal binary search, but now pretend that our search
            # key is k+epsilon, i.e. the smallest value > k.
            # YOUR CODE GOES HERE
            if k < l[mid]:
                high = mid
            else:
                low = mid + 1

    return low


def bsearch(l, k, low=None, high=None):
    """
    Binary search a list l for key k.

    Inputs:
    l is a list, possibly empty, possibly containing duplicates, that is
    ordered in non-decreasing order

    k is the value to search for in l

    low, high if present indicate the slice l[low:high] of l to search,
    ignoring the other parts of l, which might contain occurences of k.
    Default values of low is 0, high = len(l)

    Outputs:

    [ False, pos ] - the key k was not found in l[low:high].  To insert the
        k into l, place it BEFORE position pos.  That is,
        if pos = low, then l[low:high] is empty, or k < l[low]
        if pos = high, then l[high-1] < k
        otherwise l[pos-1] < k < l[pos]

    [ True, start, stop ] - the key k was found in l[low:high], and the
        slice [start:stop] contains exactly all instances of k present in
        l[low:high] (i.e. the k-range as described for bsearch_side above).

    See the doc tests below for examples.

    Complexity -
        O( log(high-low+1) )

    Doc tests:

    >>> t = []
    >>> bsearch(t, 1)
    [False, 0]
    >>> u = [3, 3]
    >>> bsearch(u, 0)
    [False, 0]
    >>> bsearch(u, 4)
    [False, 2]
    >>> bsearch(u, 3)
    [True, 0, 2]

    >>> s = [2, 2, 3, 5, 6, 7, 9, 9, 9, 10, 11, 11]
    >>> bsearch(s, 1)
    [False, 0]
    >>> bsearch(s, 2)
    [True, 0, 2]
    >>> bsearch(s, 4)
    [False, 3]
    >>> bsearch(s, 7)
    [True, 5, 6]
    >>> bsearch(s, 8)
    [False, 6]
    >>> bsearch(s, 9)
    [True, 6, 9]
    >>> bsearch(s, 10)
    [True, 9, 10]
    >>> bsearch(s, 11)
    [True, 10, 12]
    >>> bsearch(s, 12)
    [False, 12]

    Test the insertion points:

    >>> r = bsearch(s, 8)
    >>> r
    [False, 6]
    >>> if not r[0]: s.insert(r[1], 8)
    >>> s == [2, 2, 3, 5, 6, 7, 8, 9, 9, 9, 10, 11, 11]
    True

    >>> r = bsearch(s, 1)
    >>> r
    [False, 0]
    >>> if not r[0]: s.insert(r[1], 1)
    >>> s == [1, 2, 2, 3, 5, 6, 7, 8, 9, 9, 9, 10, 11, 11]
    True

    >>> r = bsearch(s, 12)
    >>> r
    [False, 14]
    >>> if not r[0]: s.insert(r[1], 12)
    >>> s == [1, 2, 2, 3, 5, 6, 7, 8, 9, 9, 9, 10, 11, 11, 12]
    True
    """

    # Default limits for search
    if low is None:
        low = 0
    else:
        low = low

    if high is None:
        high = len(l)
    else:
        high = high

    # Use the end-point search to locate the left and right positions
    # around the all k interval.
    #
    left_pos = bsearch_side(l,k, low = low, high = high)
    right_pos = bsearch_side(l,k, find_high_side=True, low = low, high = high)
    if left_pos==right_pos:
        return [flase,left_pos]
    # YOUR CODE HERE
    # HINT - use bsearch_side to find the k-range

    return [True, left_pos, right_pos]

def _test():
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    """
    Doctest non-module execution
      python3 bsearch.py --test

    Run doctests if the --test argument is in os.args, otherwise
    run as a main program.
    """
    import sys
    if "--test" in sys.argv:
        print("Running doctests")
        _test()
        exit()

    """
    Normal non-module execution
      python3 bsearch.py
    read in a list of unique integer items, not necessarily in order,
      3 6 11 9 22
    followed by a sequence of queries, one per line, like
      2
      6
    After each query print the result list from bsearch_side,
    bsearch_side (finding the high side), and bsearch, for example with
    the above you get
      2
      [False, 0]
      6
      [True, 1, 2]
    """

    line = next(sys.stdin)
    s = sorted(map(int, line.split()))

    for line in sys.stdin:
        k = int(line.strip())
        r = bsearch_side(s, k)
        print(r)
        r = bsearch_side(s, k, find_high_side=True)
        print(r)
        r = bsearch(s, k)
        print(r)
