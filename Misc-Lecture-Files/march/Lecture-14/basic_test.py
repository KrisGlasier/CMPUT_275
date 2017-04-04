# Expression trees from Wednesday class

import sys
sys.path.insert(0, "../lib")

from structviz import StructViz
from basictree import *

# t1 = BasicTree( [ 0, 2 ] )

if False:
    t0 = BasicTree()
    StructViz.update_viz(t0, "t", pause=-1)

    t0 = BasicTree( [ BasicTree(), BasicTree() ] )
    StructViz.update_viz(t0, "t", pause=-1)

if False:
    t1 = BasicTree( [ t0, t0 ] )
    StructViz.update_viz(t1, "t", pause=-1)

if True:
    print("Constructing tree from list")
    t1 = BasicTree.list_to_tree([ [], 1, 2, 3, [4, 5, [ [], []]], [ [ 6, 7]]])
    StructViz.update_viz(t1, "t", pause=-1)

    print("And making a copy")
    # Note how if you call a class method with an object, it uses the
    # class of the object to determine which class to use.
    t1_copy = t1.list_to_tree(original.get_shape())
