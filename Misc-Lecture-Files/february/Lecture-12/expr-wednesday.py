# Expression trees from Wednesday class

from structviz import StructViz

def update_dot(v, obj, basename, style='compact'):
    f = open(basename + '.dot', "w", encoding="utf-8")
    v.analyze_struct(obj)
    if style == 'compact':
        rep = v.gen_compact_dot_desc()
    else:
        rep = v.gen_detailed_dot_desc()
    f.write(rep)
    f.close()

v = StructViz()
exp = [ '*', ['+', 1, 2 ], ['+', 3, 4 ] ]
update_dot(v, exp, "tree")

# give us string rep of tree
def unparse(tree):
    if type(tree) is list:
        (oper, left, right) = tree
        return "( {} {} {} )".format(
            unparse(left),
            oper,
            unparse(right) )
        
    else:
        number = tree
        return str(number)

def topolish(tree):
    if type(tree) is list:
        (oper, left, right) = tree
        return topolish(left) + topolish(right) + [ oper ]
        
    else:
        number = tree
        return [ number ]

def stackeval(polexpr):
    stack = []
    # [1, 2, '+', 3, 4, '+', '*']
    for e in polexpr:
        print(stack)
        if type(e) is str:
            rval = stack.pop()
            lval = stack.pop()
            if e == '+':
                stack.append(lval + rval)
            elif e == '*':
                stack.append(lval * rval)
            else:
                stack.append(None)
        else:
            stack.append(e)

    print(stack)
    result = stack.pop()
    return result

debug = False
def evaluate(tree):
    debug and print("Evaluating", tree)
    if type(tree) is list:
        (oper, left, right) = tree

        lval = evaluate(left)
        rval = evaluate(right)

        if oper == '+':
            result =  lval + rval
        elif oper == '*':
            result = lval * rval
        else:
            result = None
    else:
        result = tree

    # if x < high and l[x] == 2

    debug and print("... result is", result)
    return result

# 1 2 + 3 4 + *
# print(unparse(exp))
# print(topolish(exp))
# print(evaluate(exp))

prog = topolish(exp)
print(prog)
result = stackeval(prog)
print(result)


