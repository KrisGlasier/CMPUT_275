from adjacencygraph import AdjacencyGraph
import sys

"""
Morning problem - find cycles in a digraph

A cycle in a digraph is a sequence of directed edges that forms a path
that returns to the start in vertex.  Each vertex occurs exactly once
on the cycle.  The goal of this problem is to use breadth-fist search
to find, for each vertex v, a SHORTEST length cycle that begins with
v and returns to v.  Shortest in this case means least number of edges.

The input to the program is a digraph specified in the format used
by the read_graph routine below, namely pairs of edges.

The output of the program is a sequence of lines, ordered by vertex
number. Each line begins with the vertex number, followed by a list of
the vertices in the cycle. The empty list indicates that there is no
cycle containing the vertex.

For example, on this input digraph
6 4
5 4
5 7
7 0
5 6
6 1
3 2
2 3
6 2
4 3
1 5
5 3
2 5
0 2
0 4
8 2

You would get the output

0:[0, 2, 5, 7]
1:[1, 5, 6]
2:[2, 3]
3:[3, 2]
4:[4, 3, 2, 5]
5:[5, 6, 1]
6:[6, 1, 5]
7:[7, 0, 2, 5]
8:[]

Note how the vertex 2 participates in three distinct cycles.

"""


def read_graph():
    """
    Read in a list of directed edges, one edge per line, each edge
    consisting of a from and to vertex, whitespace delimited.

    For example:
        1 3
        3 4
        4 1
        3 8

    The vertices at each end of the edge are auto-created.

    Returns:
        resulting directed graph as an instance of AdjacencyGraph
    """

    g = AdjacencyGraph()
    # for line in sys.stdin:
    for line in open('TestCase','r'):
        line = line.strip()
        if line == "" or line[0] == "#":
            continue

        (x, y) = line.strip().split()
        # Make into integers, for convenience
        x = int(x)
        y = int(y)
        g.add_edge((x, y), autocreation=True)
    return g


def find_cycle(g, v_start):
    """
    Determine a shortest cycle that includes v_start

    Inputs:
    g - an instance of an AdjacencyGraph
    v_start - starting vertex

    Returns:
    if there is no cycle, returns empty list []

    if there is a cycle, returns a list of vertices
        c = [v_0, v_1, v_2, ..., v_n-1]
    with the following properties:
        c[0] == v_start
        (c[i-1], c[i]) for 0 < i < n is an edge in g, i.e. c[i-1]->c[i]
        (c[n-1], v_start) is an edge in g, i.e. the edge
            c[n-1]->v_start completes the cycle
    """
    visited = set()

    # This is the standard breadth-first-search algorithm.  It can be
    # modified to find the shortest length cycle that returns to v_start

    # Keep track of how we got to a vertex.
    # v was reached by the edge pred[v] -> v

    pred = dict()
    queue = []
    visited.add(v_start)
    queue.append(v_start)

    while queue:
        if v_start in visited:
            break
        v = queue.pop(0)
        for w in g.neighbours(v):
            if w not in visited:
                # follow the edge v -> w
                # remember we got to w from v
                pred[w] = v
                visited.add(w)
                queue.append(w)

    # Now follow backwards from predecessor of v_start to
    # cextract the cycle.
    cycle = []
    # if v_start in visited:
    #     v = pred[v_start]
    #     while v != v_start:
    #         cycle.append(v)
    #         v = pred[v]
    #     cycle.append(v_start)
    cycle.reverse()
    return cycle


g = read_graph()

# Determine cycles for each vertex in g
for v_start in sorted(g.vertices()):
    visited = find_cycle(g, v_start)
    print("{}:{}".format(v_start, visited))
