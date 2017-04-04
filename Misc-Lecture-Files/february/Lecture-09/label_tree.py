from digraph import *
import drawgraph

# Suppose that we want to place n items into a left balanced tree.
# This is in effect doing a breadth first search of an infinite binary
# tree, where we are evenly distributing items from left to right as
# we work down the tree.

def build_tree(V, E, n):
    if n == 0:
        return

    queue = [0]
    V.add(0)
    n -= 1

    while n > 0:
        parent_v = queue.pop(0)

        left_v = parent_v * 2 + 1
        V.add(left_v)
        E.add( (parent_v, left_v) )
        queue.append(left_v)

        n -= 1
        if n <= 0:
            break

        right_v = parent_v * 2 + 2
        V.add(right_v)
        E.add( (parent_v, right_v) )
        queue.append(right_v)
        
        n -= 1
        if n <= 0:
            break

    return 
    


e_labels = { }
v_labels = { }

n = int(input("Size of tree?:"))

V = set()
E = set()

# Now construct a tree
build_tree(V, E, n)

drawgraph.render(V, E, file_name="image.dot",
    style="digraph", edge_labels=e_labels, 
    vertex_labels=v_labels, dopng=1, pause=0)
