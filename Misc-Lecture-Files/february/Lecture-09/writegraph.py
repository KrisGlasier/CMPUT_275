def write_graph_csv(G, attr=None, file_name=None):
    """
    Write out a graph expressed in csv format consisting of lines
    of the form
    V,name
    E,from,to

    where
    V lines specify a vertex
    E lines specify an edge from -> to

    Since every E line adds the mentioned vertices, there is no need for
    V lines unless you want an isolated vertex.

    file_name - name of the output file, if missing then output goes
        to stdout.

    """
    if file_name is None:
        outfile = sys.stdout
    else:
        outfile = open(file_name, 'w')

    (V, E) = G
    if attr is not None:
        (Vattr, Eattr) = attr;


    for v in V:
        if Vattr is None or v not in Vattr:
            outfile.write("V,{}\n".format(v))
        else:
            outfile.write("V,{},{}\n".format(v,Vattr[v]))

    for e in E:
        (x, y) = e
        if Eattr is None or e not in Eattr:
            outfile.write("E,{},{}\n".format(x, y))
        else:
            outfile.write("E,{},{},{}\n".format(x, y,Eattr[(x,y)]))



def write_digraph_csv(G, attr=None, file_name=None):
    write_graph_csv(G, attr=attr, file_name=file_name)
