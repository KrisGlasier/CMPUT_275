# Expression trees from Wednesday class
import sys
sys.path.insert(0, "../lib")

from structviz import StructViz
from valuetree import *

if True:
    t0 = ValueTree(42)
    StructViz.update_viz(t0, "t", pause=-1)

    t0 = ValueTree(99,  [ ValueTree(42, [ValueTree(3)]), ValueTree(88) ] )
    StructViz.update_viz(t0, "t", pause=-1)

    t0 = ValueTree('+',  [ 
        ValueTree('/', [ValueTree(3), ValueTree(4)]), 
        ValueTree(88) ] )
    StructViz.update_viz(t0, "t", pause=-1)

    t1 = ValueTree("Bad", [t0, t0])
    StructViz.update_viz(t1, "t", pause=-1)


# special cases
if False:

    t0 = ValueTree.list_to_tree([1, [43, [2, 21]], 3])
    StructViz.update_viz(t0, "t", pause=-1)

if True:
    t0 = ValueTree('*', [ 
            ValueTree('+', [ValueTree(3), ValueTree(4)]), 
            ValueTree('+', [ValueTree(7), ValueTree(11)]) 
            ])

    print("Doing pre-order")
    t0.pre_order(print)

if True:

    print("Visualizing post-order")
    StructViz.update_viz(t0, "t-init", pause=-1)
    cursor = None
    def action(n):
        cursor = n
        StructViz.update_viz({'c':cursor}, "t", pause=-1)
    t0.post_order(action)
        

