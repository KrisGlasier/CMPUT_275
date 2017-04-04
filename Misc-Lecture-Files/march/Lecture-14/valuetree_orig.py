"""
ValueTree Class

Intent is to use this to represent any tree-like thing with a value
associated with each node.

"""
# version 2, not backward compatible
__version__ = '2.0.0'


class ValueTree:

    """
    ValueTree class

    Each tree has a value, and 0 or more sub-trees called children.

    ValueTree(v) - constructs a new instance of the Tree class, with value
        v and no children.  It is a leaf.

    If each of t0, t1, ..., tn is-a ValueTree, then 
        t = ValueTree(v, [t0, t1, ..., tn] )
    constructs a new tree with value v, and children t0, t1, ..., tn

    """

    def __init__(self, value=None, children=None):

        if children is None:
            self._children = []
        else:
            self._children = children

        self._value = value

        # Check on construction that the children are # really trees.
        if not all([ type(t) is ValueTree for t in self._children ] ) :
            raise ValueError("Not every child is-a Tree")


    def pre_order(self, action):
        """
        Do a pre_order traversal of the tree, applying the action
        function to the value of each sub-tree.

        What about acting on the tree?  Like the taxo program?
        What about writing our own traversal?  What methods do we need?
        """

        action(self._value)
        for c in self._children:
            c.pre_order(action)


    def post_order(self, action):
        """
        Do a post_order traversal of the tree, first doing a post_order
        on the children, and then applying the action function to 
        self.

        """
        for c in self._children:
            c.post_order(action)
        action(self)
        

    @classmethod
    def list_to_tree(cls, l):
        """
        Convert a list into a corresponding tree
        """
        children = []
        for e in l:
            if type(e) is list:
                children.append(ValueTree.list_to_tree(e))
            else:
                children.append(ValueTree(e, []))

        return ValueTree(None, children)
        
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
