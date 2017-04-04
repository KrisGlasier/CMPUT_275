"""
ExprTree Class

General Expression Tree

"""
from valuetree import ValueTree
class ExprTree(ValueTree):

    """
    Expression tree.

    An expression tree is a ValueTree where the values in the tree are
    interpreted as follows:

    leaf nodes - have a value that is a constant object (e.g. 
        number, string, etc.)

    internal nodes - have a value that is a function object, which takes 
        the evaluated values of the children as its arguments.

    For example
        
    >>> t = ExprTree( lambda x, y: x + y, [ ExprTree(3), ExprTree(4) ] )
    >>> t.evaluate()
    7

    """

    def __init__(self, value=None, children=None):

        # The parent (super) class needs to be initialized.  It will
        # check the children for consistency
        super().__init__(children=children)

        # Now us
        self._value = value

    # Expression-related operations

    def evaluate(self):
        # No children, return the value.  Hmm, maybe having an is_empty()
        # method would be useful.

        cl = self.get_children()
        if len(cl) == 0:
            return self.get_value()

        args = [ c.evaluate() for c in cl ]

        oper = self.get_value()

        # * is the special "use list as remaining parameters" operator
        # if f(x, y, z) takes three arguments, and args = [1, 3, 5]
        # then f(*args) is the same as f(1, 3, 5)

        return oper(*args)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
