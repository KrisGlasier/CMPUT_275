def update_dot(v,obj,basename,style='compact'):
    f = open(basename + ".dot", "w", encoding="utf-8")
    v.analyze_struct(obj)
    if style == 'compact':
        rep = v.gen_compact_dot_desc()
    else:
        rep = v.gen_detailed_dot_desc()
    f.write(rep)
    f.close()
v = StructViz()
exp = ['*',['+',1,2],['+',3,4]]
update_dot(v,exp,"tree")

#give us a string rep of tree
def unparse(tree):
   if type(tree) is list:
       (oper,left,right)=tree
       return "( {} {} {} )".format(unparse(left),oper,unparse(right))
   else:
       number = tree[0]
       return str(number)

print( unparse(exp))
def evaluate(tree):
   if type(tree) is list:
       (oper,left,right)=tree
       lval = evaluate(left)
       rval = evaluate(right)
       if oper == '+':
           result = lval + rval
       if oper == '*':
           result = lval * rval
       if oper == '/':
           result = lval / rval
       if oper == '-':
           result = lval - rval
   else:
       number = tree[0]
       result =  str(number)
   return result
