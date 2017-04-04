"""
A digraph G=(V, E) is a set of vertices V, and a set of edges E
expressed as tuples over V x V, with each edge interpreted as (from, to)

So to specify a graph we just need V and E.
"""

import drawgraph

def adj_to(G, x, y):
    """
    A vertex x is adjacent to a vertex y if there is an edge from x to y
    """
    (V, E) = G
    return (x, y) in E

def to_neighbours_nc(G, v):
    (V, E) = G
    return [ y for y in V if (v, y) in E ]

# A cached map for G from v->to_neighbours(v) .  See NOTE below
neighbours_cache = dict()
def to_neighbours(G, v):
    """
    The to-neighbours of v are the ones that we can get to by following one
    edge from v. 

    The to_neighbours are defined by:
        [ y for y in V if adj_to(G, v, y) ]
    but this list comprehension is very slow.  So we pre-compute the
    neighbours of each vertex and cache them.  

    NOTE that the cache is a function of the graph, so we can only
    support one graph, and that it assumes that E is constant, so we
    cannot add and remove edges without flusing the cache.

    """
    (V, E) = G
    
    global neighbours_cache

    if len(neighbours_cache) == 0:

        for x in V:
            neighbours_cache[x] = []

        for (x, y) in E:
            neighbours_cache[x].append(y)

    return neighbours_cache[v]
