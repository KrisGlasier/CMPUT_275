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


def cycle(G, e):
    '''Returns True if adding e to edgeset E creates a cycle.'''
    (V, E) = G
    source, target = list(e)
    visited = set()

    def dfs(v):
        '''Return True if from v we can reach source.'''
        if v == source:
            return True
        visited.add(v)
        for u in neighbours(G, v):
            if u not in visited and dfs(u):
                return True
        return False

    return dfs(target)


def is_cyclic(E):
    '''Returns True if the input edgeset is cyclic.'''
    V = frozenset.union(*E)
    G = (V, E)
    visited = {v: False for v in V}

    def __is_cyclic(v, visited, parent):
        visited[v] = True
        for u in neighbours(G, v):
            # If the node is not visited then recurse on it
            if not visited[u]:
                if __is_cyclic(u, visited, v):
                    return True
            # If adjacent vertex visited and not parent of current vertex,
            # then there is a cycle
            elif parent != u:
                return True
        return False

    for v in V:
        if not visited[v]:
            if __is_cyclic(v, visited, None):
                return True

    return False

# T = set()
# for e in sorted_edges:
#     if not cycle((V, T), e):
#         T.add(e)
#
