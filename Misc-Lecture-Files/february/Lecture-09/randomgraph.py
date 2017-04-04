import random
def _n_to_c(n):
    """
    Convert number n into a base 26 character string
    """
    chars = "abcdefghijklmnopqrstuvwxyz"
    c_len = len(chars)
    s = []
    n = int(n)
    if n < 0: n = -n
    while ( True ):
        (q, r) = divmod(n, c_len)
        s.append(chars[r])
        n = q
        if n <= 0 : break
    return "".join(s)

def random_graph(n_vertices, n_edges, alpha_style=False):
    """
    Returns a random graph (V, E) with n_vertices and <= n_edges
    There are guaranteed to be no self-loops or parallel edges, but
    the small chance that a edge is generated twice means that there
    may be less that n_edges in the result.  And of course at most
    n_vertices * ( n_vertices - 1) edges can be generated.

    alpha_style = True means instead of vertex numbers use vertex names
    generated from a base 26 encoding of the lowercase letters a-z
    """
    V = set()
    for n in range(n_vertices): 
        v_name = _n_to_c(n) if alpha_style else n
        V.add( v_name )

    E = set()

    # Boundary case
    if n <= 1 : return (V, E)

    max_n_edges = n_vertices * ( n_vertices - 1)

    for n in range(min(n_edges, max_n_edges)):
        v_from = random.randrange(n_vertices)
        v_to = random.randrange(n_vertices)
        while( v_from == v_to ):
            v_to = random.randrange(n_vertices)

        v_from_name = _n_to_c(v_from) if alpha_style else v_from
        v_to_name = _n_to_c(v_to) if alpha_style else v_to
        E.add( frozenset ( (v_from_name, v_to_name) ) )

    return (V, E)

def random_digraph(n_vertices, n_edges, alpha_style=False):
    """
    Returns a random digraph (V, E) with n_vertices and <= n_edges
    There are guaranteed to be no self-loops or parallel edges, but
    the small chance that a edge is generated twice means that there
    may be less that n_edges in the result.  And of course at most
    n_vertices * ( n_vertices - 1) edges can be generated.

    alpha_style = True means instead of vertex numbers use vertex names
    generated from a base 26 encoding of the lowercase letters a-z
    """
    V = set()
    for n in range(n_vertices): 
        v_name = _n_to_c(n) if alpha_style else n
        V.add( v_name )

    E = set()

    # Boundary case
    if n <= 1 : return (V, E)

    max_n_edges = n_vertices * ( n_vertices - 1)

    for n in range(min(n_edges, max_n_edges)):
        v_from = random.randrange(n_vertices)
        v_to = random.randrange(n_vertices)
        while( v_from == v_to ):
            v_to = random.randrange(n_vertices)

        v_from_name = _n_to_c(v_from) if alpha_style else v_from
        v_to_name = _n_to_c(v_to) if alpha_style else v_to
        E.add( (v_from_name, v_to_name) )

    return (V, E)

