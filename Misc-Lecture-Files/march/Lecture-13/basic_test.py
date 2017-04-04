# Expression trees from Wednesday class

import sys
sys.path.insert(0, "../lib")

from structviz import StructViz
from basictree import *

t0 = BasicTree()
StructViz.update_viz(t0, "t", pause=-1)

t0 = BasicTree( [ BasicTree(), BasicTree() ] )
StructViz.update_viz(t0, "t", pause=-1)

t1 = BasicTree( [ t0, t0 ] )
StructViz.update_viz(t1, "t", pause=-1)

