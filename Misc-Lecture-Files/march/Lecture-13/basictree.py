"""
BasicTree Class

Intent is to use this to represent any tree-like thing.

We think of a tree is being composed of subtrees, joined together
at the root.  A tree has-a list of children.

If the list of children is empty, we say the tree is empty.

An empty tree t is constructed by
    t = BasicTree() 

If t_0, t_1, ..., t_n are Trees, then 
    t = BasicTree([t_0, t_1, ..., t_n])
constructs a tree with the given subtrees as children.
Children are ordered, left to right, in same order as the list.

Question: During construction, Can t_i and t_j be the same tree?  

Maybe yes, maybe no, depending on how the tree is going to be used. If
it is immutable, then this structure sharing would be ok. If it can be
changed, then the children being passed must be "different" or
"independent", for some meaning of this.

Pre-condition:
    The children must be "independent".

Minimal doc tests

    >>> t = Tree()
    >>> t._children == []
    True

    >>> t = Tree([1])
    Traceback (most recent call last):
    ...
    ValueError: Not every child is-a Tree

    >>> t = Tree([ Tree(), Tree() ])

"""
__version__ = '1.0.2'


class BasicTree:

    """
    BasicTree class

    BasicTree() - create a new instance of the Tree class

    """

    def __init__(self, children=None):
        """
        This method is invoked when the Tree() constructor method
        is invoked to instantiate a new instance of class Tree.
        self is bound to the newly created bare object, and then
        __init__ initializes the initial state of the object.

        All objects contain a dictionary that is used to store its
        attributes (instance variables).  You access an instance
        variable x of object o by doing o.x 

        Inside a method, this is usually self.x

        By convention, _var names are private to the object. But
        you are not prevented from touching them from outside.
        """

        if children is None:
            self._children = []
        else:
            self._children = children

        # We should check on construction that the children are
        # really trees.
        if not all([ type(t) is BasicTree for t in self._children ] ) :
            raise ValueError("Not every child is-a Tree")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
