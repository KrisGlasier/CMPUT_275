"""
A graph G=(V, E) is a set of vertices V, and a set of edges E
Each edge is a set {x, y} interpreted as being an edge between x and y.
To allow the edge to be hashed, we use frozen sets.

So to specify a graph we just need V and E.
"""

import drawgraph


def edge(x, y):
    return frozenset((x, y))


def adj(G, x, y):
    """
    A vertex x is adjacent to a vertex y if there is an edge from x to y
    """
    (V, E) = G
    return edge(x, y) in E


def neighbours(G, v):
    """
    The neighbours of v are the ones that we can get to by following one
    edge from v.
    """
    (V, E) = G
    return [y for y in V if adj(G, v, y)]


def spanning(G, root, visualize=False):
    """
    Breadth-First search to build a spanning tree
    """

    (V, E) = G

    # start with an empty spanning tree
    Te = set()

    # set of vertices already visited
    visited = set()

    # set of verticies we have not backtracked to
    queue = []

    # start by visiting the root
    visited.add(root)
    queue.append(root)

    edge_labels = {}
    if visualize:
        drawgraph.render(
            V,
            E,
            file_name="image.dot",
            style="graph",
            edge_labels=edge_labels,
            dopng=1,
            pause=-1)

    while len(queue) > 0:
        print(queue)
        v = queue[0]

        # find an unvisited w in the neighbourhood of v, and queue it up
        # for later exploration.

        for w in neighbours(G, v):
            if w not in visited:
                e = edge(v, w)

                # label edge with when it was followed, and update the
                edge_labels[e] = {"color": "red", "text": str(len(visited))}
                drawgraph.render(
                    V,
                    E,
                    file_name="image.dot",
                    style="graph",
                    edge_labels=edge_labels,
                    dopng=1,
                    pause=-1)

                # follow the edge and visit w
                visited.add(w)
                Te.add(e)

                # add w to queue to explore in the future, and keep
                # exploring v
                queue.append(w)
                break
        else:
            # loop finished without breaking out:
            # No progress made, remove v from the work queue
            del queue[0]

    # The spanning tree consists of the visited vertices plus tree edges,
    return (visited, Te)
