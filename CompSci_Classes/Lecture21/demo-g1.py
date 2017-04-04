"""
Generic demo driver for graph algorithms

This is a hack!
"""

# Import the particular implementation you want to run here
import graph_bfs_v as graph_package

if __name__ == "__main__":
    # import drawgraph
    import gengraph
    # For profiling
    import profile
    import pstats

    # Settings

    # Run the profiler, putting the stats into profile_name
    do_profile = False
    profile_name = 'profile-data.out'

    # Dump the spanning tree after running
    dump_tree = True

    (V, E) = G = gengraph.gen_graph(
              is_digraph=False,
              do_random=True,
              graph_file="test-graph-2.txt",
              do_alpha=False,
              num_vertices=10,
              num_edges=17
    )

    # pick the "first" vertex in G as root of tree
    for root in V:
        break

    print("starting at root", root)
    if do_profile:
        # Compute some profile statistics on the spanning tree alg
        profile.run('S = graph_package.spanning(G, root)',
                    filename=profile_name)
    else:
        S = graph_package.spanning(G, root, visualize=True)

    (Vs, Es) = S

    if dump_tree:
        print("spanning tree:")
        print(Vs)
        print("root:", root)
        print([sorted((x, y)) for (x, y) in Es])
        print("unvisited vertices:", V.difference(Vs))

    if do_profile:
        # See https://docs.python.org/3/library/profile.html
        # You can inspect these with command line pstats later
        p = pstats.Stats(profile_name)
        p.sort_stats('name').strip_dirs()
        p.print_stats()
        p.sort_stats('cumulative').print_stats()
