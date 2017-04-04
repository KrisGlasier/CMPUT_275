"""
Generic demo driver for graph algorithms

This is a hack!
"""
import re

# Import the particular implementation you want to run here
from min_paths import *
# from min_paths_slow import *

if __name__ == "__main__":
    import random
    import drawgraph
    import randomgraph
    import readgraph
    import writegraph

    # For profiling
    import profile
    import pstats

    # Settings


    # read: 
    # graph_file is name of file to read, if None reads from stdin
    graph_file = None
    graph_file = "test_graph.txt"
    get_attr = True

    # generate random, if not read from stdin or graph_file
    # do_alpha means generate alpha labels instead of numeric.  
    # num_vertices, num_edges give size and edge density of graph.
    do_alpha = False
    do_random = True

    num_vertices = 10
    num_edges = 17
    num_vertices = 1000
    num_edges = 15000
    num_vertices = 300
    num_edges = 1000

    # Run the profiler, putting the stats into profile_name
    do_profile = True
    profile_name = 'profile-data.out'

    # Dump the result
    dump_result = True

    if do_random:
        G = randomgraph.random_digraph(num_vertices, num_edges, 
            alpha_style=do_alpha)

        (V, E) = G

        # pick the "first" vertex in G as root of tree
        # for root in V: break;
        root = random.choice(list(V))

        Vattr = dict()
        Eattr = dict()
        
        A = (Vattr, Eattr)

        for e in E:
            Eattr[e] = random.randint(1,4)

        # save the tree in case it's interesting
        writegraph.write_digraph_csv(G, attr=A, file_name = "random_graph.txt")

    else:
        result = readgraph.read_digraph_csv(
            file_name=graph_file, get_attr=get_attr)

        # force root for example tree.
        root = 0

        # Extract out Graph and Attributes
        G = result[0:2]
        (V, E) = G
        A = result[2:4]
        (Vattr, Eattr) = A

        # On input the attributes are just strings, so turn them into
        # something useful.  
        for (k,v) in Eattr.items():
            if v == '':
                Eattr[k] = None
            else:
                Eattr[k] = int(v)

    # use the attributes to define a cost function
    def cost_fn(x, y):
        # what if
        #   return 0
        #   return -1
        return Eattr[ (x, y) ]

    if not do_profile:
        print(Eattr)
    
    if do_profile:
        # Compute some profile statistics on the spanning tree alg
        profile.run('paths = min_paths(G, cost_fn, root, visualize=False)', 
            filename=profile_name)
    else:
        paths = min_paths(G, cost_fn, root, visualize=True)

    # Shortest paths from root
    
    def display_reached(r):
        print("Resolved vertices:")
        l = [ "  {}: {}->{}".format(v[1][0], v[0], v[1][1])
            for v in sorted(r.items(), key = lambda x: x[1][0]) ]
        print("\n".join(l) )

    if dump_result and not do_profile:
        print("Paths:")
        print(paths)

    if do_profile:
        # See https://docs.python.org/3/library/profile.html
        # You can inspect these with command line pstats later
        p = pstats.Stats(profile_name)
        p.strip_dirs()
        # p.sort_stats('name').print_stats()
        p.sort_stats('cumulative').print_stats()

