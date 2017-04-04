def find_peak(hill):
    """
    Assumption: 'hill' is a nonempty list of integers with the guarantee that
    there is some index 0 <= i < len(l) such that the sublist
    hill[0:i+1] is strictly increasing and the sublist hill[i:len(l)] is
    strictly decreasing. So hill[i] is the 'peak' of the hill.

    Return the index i of this peak. Your algorithm should run in O(log n) time.

    You can assume that we will only test your implementation with
    lists that satisfy the above property.

    Examples:
    find_peak([1, 3, 6, 7, 4, 1])
    3

    find_peak([4])
    0

    find_peak([1, 2, 3])
    2

    find_peak([9, 4])
    0

    find_peak([1, 8, 6, 2])
    1
    """

    """
        This method was inspired by the bsearch algorithm we learned in class
        And was adapted to find the index of the largest value in a list of
        strictly increasing values followed by strictly decreasng values.

        Runs in O( log n ) where n is the length of "hill" list.
        Can be adapted to find the max of a list, regardless of what increases
        or decreases, but would run in O( n*log n ), since the max() function
        costs O( n ).
    """

    # Basic cases, Checking for correct types and lengths. A list with one
    # value in it is it's own peak, so return 0 for the 0th element.
    if type(hill) is not list or len(hill) == 0:
        return None
    if len(hill) == 1:
        return 0

    # Initialize variables
    low  =  0
    high =  len(hill)-1

    # Rather than search recursivley and make new lists each recurse,
    # use the same list and find your value faster!
    while low < high:
        # Compare the largest and smallest index for the larger value
        # Then shorten our indecies range.
        if hill[high-1] > hill[high]:
            high -= 1
        if hill[low+1] > hill[low]:
            low += 1

        # if the largest value reverses, we've found the peak!
        # Return the index
        if hill[high-1] < hill[high]:
            return high
        elif hill[low] > hill[low+1]:
            return low

if __name__ == "__main__":
    Expected = [3, 0, 2, 0, 1, None, None]
    Mountain = [[1, 3, 6, 7, 4, 1],
                [4],
                [1, 2, 3],
                [9, 4],
                [1, 8, 6, 2],
                {1,2,3},
                []]

    for i in range(len(Mountain)):
        ExpValue = Expected[i]
        Test = find_peak(Mountain[i])
        Bool = ExpValue == Test
        print("expected, received, True/False\t", ExpValue, Test, Bool)
