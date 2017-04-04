# Expression trees from Wednesday class
import sys
sys.path.insert(0, "../lib")

from structviz import StructViz
from exprtree import *

def op_plus(x, y):
    return x + y

def op_times(x, y):
    return x * y

# map from operator to the function that computes it
op_to_fn = {
    '+' : op_plus,
    '*' : op_times,
    }

def list_to_expr_tree(l):
    if type(l) is not list:
        # We have a constant
        return ExprTree(l)

    # We have an operation, convert the operation string, e.g. '+'
    # to its associated function, and store that as the value.  The
    # children are converted from their corresponding sub-expression

    # get corresponding function from table, None if not present.

    op = l[0]
    fn = op_to_fn.get(op)

    if fn is None:
        raise ValueError("Unimplemented operation '{}'".format(op))
        return ExprTree(None)

    return ExprTree(fn, [ list_to_expr_tree(term) for term in l[1:] ])

if False:

    print("Evaluating expression tree")
    t = ExprTree( lambda x, y: x + y, [ ExprTree(3), ExprTree(4) ] )
    StructViz.update_viz(t, "t", pause=-1)
    print("Test evaluation:",  (t.get_value())(3, 4) )
    r = t.evaluate()
    print("Result is:", r)

if True:
    from parse_expr import ExprParser

    # Input an expression, parse it into a nested-list parse tree,
    # conver to an expression tree, and then evaluate it.

    # Build a parser
    p = ExprParser()

    # Ask for an expression until get empty string
    while True:
        s = input("?")
        s = s.strip()
        if s == "": 
            break

        l = p.parse(s)

        print("Parsed expr: {}".format(l))

        convert_ok = True
        try:
            t = list_to_expr_tree(l)
        except ValueError as e:
            print("Bad conversion: {}".format(e))
            convert_ok = False

        if convert_ok:
            file_name = "t"
            print("Resulting ExprTree in '{}.dot' and '{}.dot.png'".
                format(file_name, file_name))
            disp = { 'op_to_fn' : op_to_fn, 'expr' : t }

            StructViz.update_viz(disp, file_name, 
                style='compact', pause=0, format=['png'])

            try:
                r = t.evaluate()
                print("Result is {}".format(r))
            except Exception as e:
                print("Evaluation error: {}".format(e))


    print("Done")
