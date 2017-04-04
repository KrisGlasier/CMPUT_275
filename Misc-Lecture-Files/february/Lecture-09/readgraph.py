debug = True

def read_digraph_csv(file_name=None, style='digraph', get_attr=False):
    """
    Read in a digraph expressed in csv format consisting of lines
    of the form
    V,name,v_attr
    E,from,to,e_attr

    where 
    V type lines specify a vertex
    E type lines specify an edge from -> to
    ,attr - is the remainder of the line containing additional attributes
        to be processed later.  If the , is missing, there are no attributes.

    Since every E line adds the mentioned vertices, there is no need for
    V lines unless you want an isolated vertex, or to attribute a vertex
    
    file_name - name of the input file, if missing then input comes
        from stdin.  

    style - 'digraph' to read in a digraphC (default)
            'graph' to read in a graph

    get_attr - also capture any attributes that appear with the vertex or
        edge and also return those in dictionary keyed by vertex or edge.
        default is False

    Returns a list: [V, E, Vattr, Eattr] 
        - in the case of get_attr=True.  Vattr, Eattr 
          are dictionaries keyed by vertex or edge respectively.
        - in the case of get_attr=False.  Vattr, Eattr are None

    """
    if file_name is None:
        infile = sys.stdin
    else:
        infile = open(file_name, 'r')

    if style == "graph":
        # we are doing a graph
        is_digraph = False
    elif style == "digraph":
        # default is a digraph
        is_digraph = True
    else:
        raise ValueError("style={} not supported" .format(style))

    V = set()
    E = set()
    if get_attr:
        Vattr = dict()
        Eattr = dict()
    else:
        Vattr = none
        Eattr = none

    def make_number(s):
        """
        If s represents a number, make it into one, otherwise return 
        it as a string.  We try to make it an integer first, then a
        float, and if all else fails leave it.
        """
        r = None
        try:
            r = int(s)
            return(r)
        except:
            pass

        try:
            r = float(s)
            return(r) 
        except:
            pass

        return(s)

    def fetch_token(s):
        """
        Fetch the next token in s, up to but not including the ','

        Return (t, r)
            t is the token, stripped of leanding and trailing white space
            r is the remainder of the line after the ',', unstripped
        """
        (token, s_split, rest) = s.partition(",")

        # Handle no split point
        if s_split =="":
            return(s, "")
        else:
            return(token, rest)

    for l in infile:
        # Get rid of leading and trailing white space
        l = l.strip()
        # and skip blank and comment lines
        if l == "" or l[0] == "#":
            continue

        # Break into tokens at commas

        # Fetch type of line
        (line_type, l) = fetch_token(l)

        if line_type == "V":
            (v, l) = fetch_token(l)
            V.add(make_number(v))

            if get_attr:
                Vattr[v] = l

        elif line_type == "E":
            (x, l) = fetch_token(l)
            (y, l) = fetch_token(l)
            x = make_number(x)
            y = make_number(y)

            if is_digraph:
                e = (x, y) 
            else:
                e = frozenset( (x, y) )

            E.add( e )

            # What if a vertex is not in V?  Add it.
            V.add(x)
            V.add(x)

            if get_attr:
                Eattr[e] = l

        else:
            raise ValueError("Bad line type {}", line_type)

        
    if debug:
        print("Num vertices:", len(V))
        print("Num edges:", len(E))
        print(V)
        print(Vattr)
        print("")
        print(E)
        print(Eattr)
        print("")
        
    return [V, E, Vattr, Eattr]
