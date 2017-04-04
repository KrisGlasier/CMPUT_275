from structviz import StructViz


def update_dot(v, obj, basename, style='compact', do_png=False):
    """
        Wrapper for data srtucture visualization.  If you call this everytime
        you update the data structure obj then the the graphviz dot file will
        be regenerated, and the view will update.

        Inputs:
        v - an instance of a StructViz object, created with
            v = StructViz()
        obj - object to be visualized
        basename - base name of the file to be generated, will result in
            basename.dot in the current working directory
        style - rendering style, normally you want the default 'compact'
        do_png - if true also calls dot to create a rendering of the graph,
            and places it in basename.png
    """

    import subprocess

    dotname = basename + '.dot'
    f = open(dotname, "w", encoding="utf-8")
    v.analyze_struct(obj)
    if style == 'compact':
        rep = v.gen_compact_dot_desc()
    else:
        rep = v.gen_detailed_dot_desc()
    f.write(rep)
    f.close()

    if do_png:
        # now generate the image file and it will be refreshed
        subprocess.call(["dot", "-Tpng", dotname, "-O"])


def get_yes_no(question):
    """
        Return a yes (True) or no (False) answer to the supplied question.
    """
    while True:
        print(question + " [y|n]")
        answer = input()
        answer = answer.strip().lower()
        if len(answer) > 0:
            if answer[0] == 'y':
                return True
            if answer[0] == 'n':
                return False

        print("Please answer yes or no ...")


def get_nonblank_str(question):
    """
        Return a non-blank answer to the supplied question.
    """
    while True:
        print(question)
        answer = input()
        answer = answer.strip()
        if len(answer) > 0:
            return answer

        print("Please provide a non-blank answer ...")


def identify_thing(tree):
    """
        This function takes a taxonomy tree and attempts to identify
        a thing by asking a series of questions.  If the thing can
        be identified, it provides the name of the thing.  If the thing
        cannot be identified, then it asks for the name of the thing,
        and a distinguishing question.  In the latter case, tree is
        modified to contain the new information.

        A taxonomy tree T is a decision tree structured as follows.

        Each internal vertex (or node) of the tree corresponds to a
        discrimination question, that determines a characteristic,
        such as "Does it have 4 legs?"

        It has this structure:
          [ "D", question, T_yes, T_no ]
        where question is a string that poses a question and expects a
        Yes or No answer.  Depending on the answer, the decision path
        navigates down the yes or no decision sub tree.

        Each leaf node of the tree is an identification question,
        which confirms that a particular object with the given name has
        been identified.

        It has the structure:
          [ "I", name ]
    """

    node_type = tree[0]
    if node_type == "D":
        (question, yes_tree, no_tree) = tree[1:]
        yes_answer = get_yes_no(question)
        if yes_answer:
            identify_thing(yes_tree)
        else:
            identify_thing(no_tree)

    elif node_type == "I":
        name = tree[1]
        question = "Is it a {}?" .format(name)

        yes_answer = get_yes_no(question)
        if yes_answer:
            print("{} Identified!" .format(name))
        else:
            print("I don't know what it is.")
            new_name = get_nonblank_str("What is it?")

            new_question = get_nonblank_str(
                "Give me a question where yes means a '{}'"
                " and no means a '{}'"
                .format(new_name, name))

            # Now at this point we need to update the tree to store the
            # new information.
            # THIS IS WHERE YOU ADD YOUR TREE UPDATE CODE
            tree.pop()
            tree.pop()
            tree.append("D")
            tree.append(new_question)
            tree.append(["I", new_name])
            tree.append(["I", name])


def do_things(tree):
    """
        Given the taxonomy tree, print out a list of all the things
        identified in the tree.  The list should be in increasing
        lexicographical order with no duplicates.
    """
    S = set()

    def get_things(tree):
        if type(tree) == list:
            for X in tree:
                if X[0] == 'I':
                    S.add(X[1])
                else:
                    get_things(X)
        return
    get_things(tree)
    Q = " ".join(sorted(S))
    print(Q)
    # process and print


def do_identify(tree, do_structviz=False):
    """
        Perform the interactive thing identification.
        do_structviz=True means to output the potentially updated
        taxonomy tree.
    """
    while get_yes_no("Continue identification?"):
        print("Identify your thing")
        identify_thing(tree)
        if do_structviz:
            update_dot(v, tree, "tree")


def _test():
    e_structviz = True
    import doctest
    doctest.testmod()


def main():
    import argparse
    parser = argparse.ArgumentParser(
        description='Taxonomy service.',
        formatter_class=argparse.RawTextHelpFormatter,
    )

    parser.add_argument("-s",
                        help="Name of startup taxonomy database.",
                        nargs="?",
                        type=str,
                        dest="taxo_startup_file",
                        )

    parser.add_argument("-u",
                        help="Name updated taxonomy database.",
                        nargs="?",
                        type=str,
                        dest="taxo_update_file",
                        )

    parser.add_argument("--things",
                        help="Display ordered list of things in the taxonomy.",
                        action="store_true",
                        dest="do_things")

    parser.add_argument("--doctest",
                        help="Run doctests instead.",
                        action="store_true",
                        dest="do_doctest")

    parser.add_argument("--viz",
                        help="Enable data structure visualization.",
                        action="store_true",
                        dest="do_structviz")

    args = parser.parse_args()

    # To run doctest instead of normal interactive service
    global enable_structviz
    if args.do_doctest:
        print("Running doctests")
        enable_structviz = False
        _test()
        exit()

    # Read in the taxonomy tree
    if args.taxo_startup_file:
        f = open(args.taxo_startup_file, "r", encoding="utf-8")
        # DANGER DANGER eval of external string
        tree = eval(f.read())
        f.close
    else:
        # A default testing tree
        tree = ['D', 'Does it have 4 legs?',
                ['D', 'Can you ride it?', ['I', 'horse'], ['I', 'dog']],
                ['D', 'Does it have hands?', ['I', 'monkey'], ['I', 'bird']]]

        # Another testing tree with two instances of horse.
        tree = ['D', 'Does it have 4 legs?',
                ['D', 'Can you ride it?', ['I', 'horse'],
                 ['D', 'Was it a puppy?', ['I', 'dog'], ['I', 'horse']]],
                ['D', 'Does it have hands?', ['I', 'monkey'], ['I', 'bird']]]

    # For visualization

    if args.do_structviz:
        v = StructViz()
        update_dot(v, tree, "tree", do_png=True)

    if args.do_things:
        do_things(tree)

    else:
        do_identify(tree, args.do_structviz)

    # Dump out the updated tree if requested
    if args.taxo_update_file:
        f = open(args.taxo_update_file, "w", encoding="utf-8")
        f.write(str(tree))
        f.write("\n")
        f.close


if __name__ == "__main__":
    main()
