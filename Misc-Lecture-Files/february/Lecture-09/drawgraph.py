import subprocess
import time
import re
"""
Graph/Digraph drawing facility.

Takes a graph or digraph defined by a set of verticies v and edges e, 
and uses graphviz to render it.

The rendering produces a graphviz dot language file, which can then
optionally be used to render a .png file. Depending on the available
viewing tools, the graph can be updated dynamically, thus enabling the
visualization of an algorithm.

When provided with the dictionaries vertex_labels and edge_labels that 
map verticies and edges to associated properties, the color and labelling
can be modified.  

"""

def _make_label( label ):
    """ 
    return a list of graphviz attributes suitable for annotating a vertex
    or edge.
    """

    result = [ ]

    if 'color' in label:
        result.append('color=' + label['color'])

    if 'text' in label:
        # make sure text is in " ", and that any characters that 
        # are special to graphviz are escaped 
        result.append('label="' + _esc_dot_specials(label['text']) + '"')

    return result

def _esc_dot_specials(v):
    """
    Escape each of the following chars <>|[]\;{} that are used
    by a .dot file for the label descriptions.
    """
    v = str(v)
    r = re.sub(r'[<>"|[\]\\{};]', (lambda m: "\\" + m.group(0)), v)
    return r


def render(vertices, edges,
    file_name=None,
    style="digraph",
    vertex_labels = {}, edge_labels = {}, pause=0, dopng = False):

    """

    file_name - name of the output file, if missing then output goes 
        to stdout.  stdout precludes using the dopng option.

    vertices - any iterable collection of hashable objects

    edges - for a digraph, any iterable collection of hashable 2-tuples, 
        (from, to), where from and to are in vertices.

        - for a graph, any iterable collection of hashable 2-collections,
        {x, y} representing an edge between x and y.  At present the 
        only hasable 2-collections are frozen sets.
    
    style - "digraph" edges have direction, "graph" edges have no 
        direction.  

    vertex_labels - dictionary mapping vertex to properties

    edge_labels - dictionary mapping edge to properties

    pause - the amount of time to sleep after updating the drawing.  
        0 means no delay
        >0 means delay in seconds
        <0 means wait for user to provide a line (ignored) on stdin 
           before proceeding

    dopng - if True after generating the output file, render it into 
        a .png If the file_name is "graph.dot" then png file will 
        be "graph.dot.png"
    
    Note:  For vertex_labels and edge_labels to work, vertices and 
    edges must be hashable.  The attributes in the dictionary used 
    for rendering are:

    'color' - vertex/edge is drawn in that color
    'text'  - vertex/edge is annotated with that text

    """

    if file_name is None:
        outfile = sys.stdout
        if dopng:
            raise ValueError("Cannot have dopng option when writing to stdout.")
    else:
        outfile = open(file_name, 'w')

    if style == "graph":
        # we are doing a graph
        outfile.write('graph g {\n')
        edge_style = " -- "
        is_graph = True
        # raise ValueError("Sorry, only handle digraphs at this time.")
    elif style == "digraph":
        # default is a digraph
        outfile.write('digraph g {\n')
        edge_style = " -> "
        is_graph = True
    else:
        raise ValueError("style={} not supported" .format(style))

    # ordering not always understood, for future use
    # lr means order l to r by vertex number
    outfile.write('  ordering=lr;\n')

    # default vertex and edge attributes
    outfile.write('  node [shape=ellipse, style=filled, color=grey];\n')
    outfile.write('  edge [style="setlinewidth(3)"];\n')

    # output all the vertices to get their attributes, put them 
    # into order - this could fail so sort as strings
    # for v in sorted(vertices, key=lambda x: str(x)):
    for v in sorted(vertices):
        # get text label and color attributes
        if v in vertex_labels:
            label =  vertex_labels[v]
        else:
            label = { }

        # join them into a comma delimited list
        attr = ", ".join( _make_label( label ) )

        # attribute if we have some
        if attr != '': attr = '[' + attr + ']'

        # format of a vertex
        outfile.write( str(v) + ' ' + attr + ';\n')

    # output all the edges
    for e in edges:
        (v_from, v_to) = e

        # get text label and color attributes
        if e in edge_labels:
            label = edge_labels[e]
        else:
            label = { }

        # join them into a comma delimited list
        attr = ", ".join( _make_label( label ) )

        # attribute if we have some
        if attr != '': attr = '[' + attr + ']'

        # format of an edge depends if directed or not
        outfile.write( 
            str(v_from) + edge_style + str(v_to) + ' ' + attr + ';\n')

    # end of the dot description
    outfile.write("\n}")
    outfile.close()

    # Convert .dot file to .png for display if requested.
    # Re-generate the image file and it will be refreshed
    if dopng:
        subprocess.call(["dot", "-Tpng", file_name, "-O"])

    # wait for user to proceed
    if pause < 0: 
        s = input('\n<CR> to continue')
    elif pause > 0:
        time.sleep(pause)
        

