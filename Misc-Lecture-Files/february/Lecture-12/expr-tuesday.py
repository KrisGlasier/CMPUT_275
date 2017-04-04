# Expression trees from Tuesday class

e = [ [1, '+', 2], '*', [3, '+', 4]]

def unparse(expr):
    """
    """

    if not type(expr) is list:
        return str(expr)

    (lexpr, oper, rexpr) = expr

    return '(' + unparse(lexpr) + ' ' + oper + ' ' + unparse(rexpr) + ')'

def revpolish(expr):
    """
    """

    if not type(expr) is list:
        return str(expr)

    (lexpr, oper, rexpr) = expr

    return '(' + revpolish(lexpr) + ' ' + revpolish(rexpr) + ' ' + oper + ')'


def postorder(expr):
    """
    """

    if not type(expr) is list:
        return [ expr ]

    (lexpr, oper, rexpr) = expr

    return postorder(lexpr) + postorder(rexpr) + postorder(oper)

def posteval(postorder):
    stack = []
    for e in postorder:
        print("e: {}, stack: {}".format(e, stack))

        if e == '+':
            rhs = stack.pop()
            lhs = stack.pop()
            stack.append(rhs+lhs)

        elif e == '*':
            rhs = stack.pop()
            lhs = stack.pop()
            stack.append(rhs*lhs)

        else:
            stack.append(e)

    print("final stack", stack)
    return stack.pop()

def evaluate(expr):
    if not type(expr) is list:
        return expr
    
    (lexpr, oper, rexpr) = expr

    lvalue = evaluate(lexpr)
    rvalue = evaluate(rexpr)

    if oper == '+':
        return lvalue + rvalue
    if oper == '*':
        return lvalue * rvalue

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    print(unparse(e))
    print(revpolish(e))
    print(postorder(e))
    print(evaluate(e))

    print(posteval(postorder(e)))

    # print("Running doctests")
    # _test()

    
