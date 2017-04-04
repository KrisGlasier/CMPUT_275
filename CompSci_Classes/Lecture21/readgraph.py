import sys


def read_graph_csv(file_name=None):
    """
    Read in a graph expressed in csv format consisting of lines
    of the form
    V,name
    E,from,to

    where
    V lines specify a vertex
    E lines specify an edge from -> to

    Since every E line adds the mentioned vertices, there is no need for
    V lines unless you want an isolated vertex.

    file_name - name of the input file, if missing then input comes
        from stdin.

    """
    if file_name is None:
        infile = sys.stdin
    else:
        infile = open(file_name, 'r')

    V = set()
    E = set()

    for l in infile:
        # Get rid of leading and trailing white space
        l = l.strip()

        # Break into tokens at commas
        tokens = l.split(",")

        if tokens[0] == "V":
            V.add(tokens[1])
        elif tokens[0] == "E":
            # What if a vertex is not in V?  Add it.
            E.add(frozenset((tokens[1], tokens[2])))
            V.add(tokens[1])
            V.add(tokens[2])

    print("Num vertices:", len(V))
    print("Num edges:", len(E))

    return (V, E)


def read_digraph_csv(file_name=None):
    """
    Read in a digraph expressed in csv format consisting of lines
    of the form
    V,name
    E,from,to

    where
    V lines specify a vertex
    E lines specify an edge from -> to

    Since every E line adds the mentioned vertices, there is no need for
    V lines unless you want an isolated vertex.

    file_name - name of the input file, if missing then input comes
        from stdin.

    """
    if file_name is None:
        infile = sys.stdin
    else:
        infile = open(file_name, 'r')

    V = set()
    E = set()

    for l in infile:
        # Get rid of leading and trailing white space
        l = l.strip()

        # Break into tokens at commas
        tokens = l.split(",")

        if tokens[0] == "V":
            V.add(tokens[1])
        elif tokens[0] == "E":
            # What if a vertex is not in V?  Add it.
            E.add((tokens[1], tokens[2]))
            V.add(tokens[1])
            V.add(tokens[2])

    print("Num vertices:", len(V))
    print("Num edges:", len(E))

    return (V, E)
