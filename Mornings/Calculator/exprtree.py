"""
ExprTree Class

General Expression Tree

"""
from valuetree import ValueTree

# If you need some utility functions for the class, just put them here
# and they can be called from the class.

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
        super().__init__(value, children)

    # Expression-related operations

    def evaluate(self):
        # No children, return the value.  Hmm, maybe having an is_empty()
        # method would be useful.

        # Define the lambda expressions and their inverse
        op_to_fn = {
            'neg': (lambda x: -x),
            '+': (lambda x, y: x + y),
            '-': (lambda x, y: x - y),
            '*': (lambda x, y: x * y),
            }

        fn_to_op = dict([(v, k) for k, v in op_to_fn.items()])

        cl = self.get_children()
        if len(cl) == 0:
            return self.get_value()

        args = [c.evaluate() for c in cl]

        oper = self.get_value()
        oper = op_to_fn.get(oper)

        # * is the special "use list as remaining parameters" operator
        # if f(x, y, z) takes three arguments, and args = [1, 3, 5]
        # then f(*args) is the same as f(1, 3, 5)

        return oper(*args)

    def unparse(self):
        """
        >>> t = ExprTree.parse("1 + (3 * 4)")
        >>> t.unparse()
        '(1 + (3 * 4))'

        """
        # Get children, if they exist format them into the format of either
        # (Negation Expression) or (Expression Operation Expression)
        Lst = self.get_children()
        if len(Lst) == 0: # No Children- Only integar in Value
            return self.get_value()
        elif len(self.get_children()) == 1:
            # One number, therefore Negation operation and an expression
            Opera = self.get_value()
            LSide = Lst[0].unparse()
            str_rep = "({} {})".format(Opera, LSide)
        else:
            # Assume typical two Expressions and an opperation.
            RSide = Lst[0].unparse()
            Opera = self.get_value()
            LSide = Lst[1].unparse()

            str_rep = "({} {} {})".format(RSide, Opera, LSide)

        # Had an error that didn't work properly... So I replaced the
        # 'neg' with a subtraction sign. Doesn't affect "evaluate"
        return str_rep.replace("neg", "-")

    # This will hold the single instance of the parser
    parser = None

    @classmethod
    def parse(Cls, s):
        """
        Parse the string s into an ExprTree

        >>> t= ExprTree.parse("1 + 2")

        """

        from parse_expr import ExprParser

        # Create a singleton instance of the parser.
        if ExprTree.parser is None:
            ExprTree.parser = ExprParser()

        Chk = ExprTree.parser
        Tmp = Chk.parse(s)

        if type(Tmp) is not list:
            Result = ExprTree(Tmp)
        else:
            # Mess of code, used a recursive function to deal with it
            Result = Cls.CheckRecursive(Tmp)

        return Result

    @classmethod
    def CheckRecursive(Cls, Inst):
        """
            Returns a list of expression trees, evaluating the list possibility
            from Cls.parse()
        """

        # Integar -> One value
        if type(Inst) is int:
            return ExprTree(Inst)

        # Negation -> One value (-) and one child (Expression)
        elif len(Inst) == 2:
            ChkPar = Inst.pop(0)
            Rec1 = Inst.pop(0)
            return ExprTree(ChkPar, [Cls.CheckRecursive(Rec1)])

        # Regular Espression -> One value (Operation) and
        # two children (Expressions)
        else:
            ChkPar = Inst.pop(0)
            Rec1 = Inst.pop(0)
            Rec2 = Inst.pop(0)
            return ExprTree(ChkPar,
                            [Cls.CheckRecursive(Rec1),
                             Cls.CheckRecursive(Rec2)])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
