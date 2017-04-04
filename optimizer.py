"""
Optimizer method to be hooked into a Compiler instance

It will be invoked just as if it was defined as an instance method.
That is:
        self.ast_optimize(ast)
As an instance method it has access to other data in the Compiler object,
which is usually necessary for optimization purposes.
"""


def ast_optimizer(self, ast):
    from valuetree import ValueTree

    def ast_optimize_r(ast):
        """
        Simple dummy example of the optimizer for multiple negations.

        If it was working, this
            x = 1 + (y = (x = (x - - - - 3) + - - - - y))
        could be optimized to
            x = 1 + (y = (x = (x - -3) + y))
        or even
            x = 1 + (y = (x = (x + 3) + y))

        """

        if self.debug:
            print("Optimizing children")

        # We are basically looking for apply of neg - apply of neg
        # sequences in the AST.  A full implementation  will look
        # something like this.

        children = ast.get_children()

        if ast.get_value() == 'apply':
            # optimize each of the children (after the op)
            for c in children[1:]:
                ast_optimize_r(c)

            # after that, see if we are a double neg, any double negs in the
            # tree below are optimized at this point

        elif ast.get_value() == 'set':
            ast_optimize_r(children[1])

    # Start the optmizer recursion
    if self.debug:
        print("Optimizing for repeated negations")
        print("Before:", ast.tree_to_valshape())

    ast_optimize_r(ast)

    if self.debug:
        print("After:", ast.tree_to_valshape())
