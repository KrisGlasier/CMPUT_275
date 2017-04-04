"""
A digraph G=(V, E) is a set of vertices V, and a set of edges E
expressed as tuples over V x V, with each edge interpreted as (from, to)

Attributes A=(Vattr, Eattr) is a pair of dictionaries that map elements
of v to an attribute, and elements of e to an attribute.

So to specify a graph we just need V and E.
"""

from digraph import *
import drawgraph
import re
from minheap import MinHeap

def display_reached(r):
    print("Resolved vertices:")
    l = [ "  {}: {}->{}".format(v[1][0], v[1][1], v[0]) 
        for v in sorted(r.items(), key = lambda x: x[1][0]) ]
    print("\n".join(l) )

def display_pending(r):
    return
    print("Pending events:")
    l = [ "  {}: {}->{}".format(v[0], v[1], v[2]) 
        for v in sorted(r, key = lambda x: x[0]) ]
    print("\n".join(l) )

def min_paths(G, cost, root, visualize = True):
    """
    Use Dijkstra's algorithm to compute a min cost path from root 
    to all vertices reachable from root by a directed path.

    G=(V, E) specifies the graph

    cost(x, y) is a function which takes an edge and returns the cost of 
        following edge x -> y. cost returns None if there is no edge.

    One way of viewing this algorithm is as a discrete event simulation
    of a relay race through the graph.

    Runners are positioned at vertices ready to take a baton handoff.  The
    first runner to arrive at a vertex triggers a number of runners to
    start running, one runner for each edge leaving the vertex.  When a 
    runner arrives at their destination they stop.  If a runner arrives
    at a vertex that has already had a runner arrive, the later runner
    simply stops, and does not trigger other runners to leave.
    The first runners to arrive at a vertex establishes the minimum time 
    to rach that vertex from root.  Note that more than one runner
    can arrive simultaneously.

    The race is begun at time 0 by having the first runner dropped
    onto the root, thus triggering an number of runners to leave on the
    outgoing edges of the vertex.

    To keep track of the runners, each running runner is associated 
    with an event (t_arrive, v_from, v_to) which is interpreted as 
    the runner running on the edge v_from -> v_to will arrive at
    v_to at time t_arrive.

    All the running runners are kept in a collection of future events.

    The simulation loop is this:
        while there are runners:
            pick a runner with the smallest t_arrive, and
            process their event.

    When there are no active runners, the simulation is finished.
    """

    (V, E) = G

    # To keep track of when the first runner reached a verted we 
    # have the map reached from vertex v_to -> (t_arrive, v_from) 
    # which says that vertex v_to was reached at time t_arrive 
    # by a runner from vertex v_from
    reached = dict()

    # runners is a set of events (t_arrive, v_from, v_to) 
    # as described above

    # To start, we drop one runner onto the root, running from 
    # root to root.
    runners=MinHeap()
    runners.add(0, (0, root, root))

    # For visualization
    e_labels = { }
    v_labels = { }

    if visualize:
        v_labels[root] = {
            "color" : "red",
            "text" : str(root)
             }
        for e in E:
            (x, y) = e
            c = cost(x, y)
            e_labels[e] = { 
                "text" : str(c) + "/?"
                }

        drawgraph.render(V, E, file_name="image.dot",
            style="digraph", edge_labels=e_labels, 
            vertex_labels=v_labels, dopng=1, pause=-1)

        print("Starting at root {}" . format(root) )

    max_events = 0;
    while len(runners) > 0:
        max_events = max([max_events, len(runners)])

        # Find the runner with the smallest t_arrive. Profiling shows
        # that this is the most expensive operation in the algorithm,
        # roughly 96% of the time on 300 vertices and 1000 edges.
        # What is it's complexity?

        (key, first_runner) = runners.pop_min()

        (t_arrive, v_from, v_to) = first_runner

        if visualize:
            print("Arrival event {}: {}->{} "
                .format(t_arrive, v_from, v_to) )

        # remove the runner from the events
        # runners.remove(first_runner)

        if v_to in reached:
            # a runner made it there at time <= t_arrive
            if visualize:
                print("   but {} was reached earlier" . format(v_to))
            continue

        # first to arrive at v_to came from v_from
        reached[v_to] = (t_arrive, v_from)

        # now hand off to the waiting runners
        for v_next in to_neighbours(G, v_to):
            # Add a new runner event for each outgoing edge v_to -> v_next
            # provided that v_next has not been reached already.
            if v_next in reached:
                if visualize:
                    print("   skipping {} reached earlier" . format(v_next))
                continue

            # It takes time cost(v_to, v_next) to travel the edge, so
            # the arrival time at n is:

            runners.add(t_arrive, 
                (t_arrive + cost(v_to, v_next), v_to, v_next) )

        if visualize:
            display_reached(reached)
            display_pending(runners)

            # label edge with arrival at end point
            e = (v_from, v_to)
            if e in e_labels:
                t = e_labels[(v_from, v_to)]["text"]
            else:
                t = "?/?"

            e_labels[(v_from, v_to)] = { 
                "color" : "red",
                "text" : t[:-1] + str(t_arrive)
                 }
            v_labels[v_to] = {
                "color" : "red",
                "text" : str(v_to) 
                 }
            
            drawgraph.render(V, E, file_name="image.dot",
                style="digraph", edge_labels=e_labels, 
                vertex_labels=v_labels, dopng=1, pause=-1)

        # End of the simulation loop

    if visualize:
        display_reached(reached)

    if False:
        print("Max length of event set", max_events)
    return reached
