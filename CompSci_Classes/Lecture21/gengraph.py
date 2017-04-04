import randomgraph
import readgraph


def gen_graph(is_digraph=False,
              do_random=True,
              graph_file="test-graph-2.txt",
              do_alpha=False,
              num_vertices=10,
              num_edges=17
              ):
    '''Generates a graph to be used for testing.

    Args:
        is_digraph (bool): Whether the graph to be generated or read
            should be a digraph.
        do_random (bool): If True, generates graph at random, otherwise
            reads from graph_file.
        graph_file: Either str (filename), None. If None, reads graph
            from stdin. Only effective if do_random=False.

        The next arguments are only effective if do_random=True.

        do_alpha (bool): generate alpha labels instead of numeric.
        num_vertices (int): number of vertices to be generated.
        num_edges (int): number of edges to be generated.

    Returns:
        G = (V,E), a graph with the chosen properties. V is vertex-set
            and E is an edge set of pairs of vertices.
    '''

    # random:
    #   num_vertices, num_edges give size and edge density of graph.

    if is_digraph:
        if do_random:
            G = randomgraph.random_digraph(
                num_vertices, num_edges, alpha_style=do_alpha)
        else:
            G = readgraph.read_digraph_csv(file_name=graph_file)
    else:
        if do_random:
            G = randomgraph.random_graph(
                num_vertices, num_edges, alpha_style=do_alpha)
        else:
            G = readgraph.read_graph_csv(file_name=graph_file)

    (V, E) = G

    return G
