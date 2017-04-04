class Box:
    def __init__(self, x, y, w, h):
        '''
        Create an instance of the box class whose lower-left corner is at (x,y)
        and whose width is w and height is h. The width w and height h must be
        positive.
        '''

        if w <= 0 or h <= 0:
            raise ValueError("cannot create box with nonpositive dimensions")
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def moveBy(self, dx, dy):
        '''
        Translates this box by dx units along the x axis and dy units along
        the y axis.
        '''
        self.x += dx
        self.y += dy

    def contains(self, b):
        '''
        Assumes b is another instance of the box class.

        Returns true if and only if the box b is entirely contained
        within box self (they can share edges).
        '''
        return (self.x <= b.x and self.y <= b.y and
                self.x + self.w >= b.x + b.w and
                self.y + self.h >= b.y + b.h)

    def unionWith(self, b):
        '''
        Assumes b is another instance of the box class.

        Returns the smallest box that contains both self and box b.
        '''
        new_x = min(self.x, b.x)
        new_y = min(self.y, b.y)
        new_w = max(self.x + self.w, b.x + b.w) - new_x
        new_h = max(self.y + self.h, b.y + b.h) - new_y
        return Box(new_x, new_y, new_w, new_h)

    def __str__(self):
        return "Box({}, {}, {}, {})".format(self.x, self.y,
                                            self.w, self.h)


def longest_sequence(boxes, i, memo = None):
    '''
    Assumes boxes is a list of boxes and that no two boxes have identical
    (x,y,w,h) (i.e. no two boxes are the same). Also, 0 <= i < len(boxes) is an index.

    Returns the largest value m such that it is possible to find a list of length m
    of distinct boxes starting at boxes[i] where each box in the list contains
    the next box in the list (according to the contains() method).

    Note, the boxes in "chain" don't have to be in the same order as they
    appeared in boxes.

    Example:
    boxes = [Box(3, 3, 7, 7), Box(1, 1, 10, 10), Box(2, 2, 5, 5)]
    longest_sequence(boxes, 1) returns 2

    boxes2 = [Box(3, 3, 7, 7), Box(1, 1, 10, 10), Box(2, 2, 8, 8)]
    longest_sequence(boxes, 1) returns 3

    For full marks, your algorithm should run in O(n^2) time where
    n = len(boxes). Use dynamic programming to achieve this.
    '''
    FirstCall = False
    if memo is None:
        FirstCall = True
        memo = dict()

    # Base Cases:
    if len(boxes) == 0:
        return 0
    elif len(boxes) == 1:
        memo[boxes[0]] = 1
        return max(memo.values()) # Max() speeds up computation

    # Scan through all the boxes, remove those that are
    # outside the current box to speed computation later
    temp = []
    for j in boxes:
    	if boxes[i].contains(j):
        	temp.append(j)

    # Inititalize memory values, and sort the boxes according to
    #   a) Start location (x,y) coordinates
    #   b) Reciprocal of height and width (1/h, 1/w)
    memo.setdefault(boxes[i], [ boxes[i] ])
    boxes = sorted(temp, key=lambda box:(box.x, box.y, 1/box.h, 1/box.w))

    # Current box we're looking at and it's size
    currentBox = boxes[0]
    currentSize = len(memo[currentBox])

    # Scan through the boxes and initialize it's memory.
    for BoxIndex in range(len(boxes)):
        memo.setdefault(boxes[BoxIndex], [])
        nextBox = boxes[BoxIndex]
        NextSize = len(memo[nextBox])
        # Check if our current box contains the next box
        if currentBox.contains(nextBox) and currentBox != nextBox:
            # If it is inside, set memory to the memory of current box +
            # next box.
            if NextSize < currentSize+2:
                memo[nextBox] = memo[currentBox] + [nextBox]
            longest_sequence(boxes, BoxIndex, memo)

    # Look through all the lengths of each dictionary path and return the
    # length of the longest path.
    if FirstCall:
        return sorted([len(i) for i in memo.values()])[-1]

# State the running time of your algorithm below here. Justify it in 2-3
# sentences. Hint, remember the "running time analysis template" for dynamic
# programming problems from the lectures.

# I believe this function has a Big O notation that approximates to
# O(n^2 + n) where n is the length of the initial array of boxes. This would
# be because I use the sorted() function twice. The first one sorts through
# an ever shortening array as we go farther in the recursion. Secondly, the
# last line of my function sorts through my memo dictionary and then organizes
# the values from smallest to largest. The two of these I approximate to be of
# n cost since the first gets faster the farther we go and the second is run
# once. Not sure how to get O(n^2), any tips?

if __name__ == "__main__":
    # Testing the function with 5 test cases
    EmptyBoxes = []
    print("Empty list: ",longest_sequence(EmptyBoxes, 0),"\r\n")
    OneBox = [Box(1, 1, 1, 1)]
    print("Single item list: ",longest_sequence(OneBox, 0),"\r\n")

    print("Testing 5 sets of boxes, evaluating the 2nd element in each (index 1)")
    boxes = [[Box(3, 3, 7, 7), Box(1, 1, 10, 10), Box(2, 2, 5, 5)],
        [Box(3, 3, 7, 7), Box(1, 1, 10, 10), Box(2, 2, 8, 8)],
        [Box(1, 1, 4, 4), Box(2, 2, 2, 2), Box(2, 2, 1, 2), Box(3, 2, 1, 1)],
        [Box(1, 1, 4, 4), Box(2, 2, 2, 2), Box(2, 2, 1, 1), Box(2, 2, 1, 2)],
        [Box(1, 1, 4, 4), Box(2, 2, 2, 2), Box(2, 2, 1, 1), Box(2, 2, 1, 2), Box(2, 2, 2, 1)]]
    expected = [2,3,2,3,3]

    for i in range(len(boxes)):
        print("Test {}: ".format(i+1), longest_sequence(boxes[i],1),
            " Expected: {}".format(expected[i]))

    for i in range(len(boxes)):
        print("\r\nPossible cases for test {}: ".format(i+1))
        for j in range(len(boxes[i])):
            print("\t Index {}: ".format(j+1, j), longest_sequence(boxes[i],j))
