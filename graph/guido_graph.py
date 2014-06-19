# Example from https://www.python.org/doc/essays/graphs/
"""graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}"""

graph = {}


def nodes():
    """return list of all nodes in graph"""
    return graph.keys()


def edges():
    """return list of all edges in graph"""
    pass


def add_node():
    """adds new node 'n' to graph"""
    pass


def add_edge(n1, n2):
    """"adds new edge to graph connecting n1 and n2
        if either n1 or n2 are not already in graph, adds them"""
    pass


def del_node(n):
    """deletes node n from graph
       raises error if no such node exists"""
    pass


def del_edge(n1, n2):
    """deletes edge containing n1 and n2 from graph
       raises error if no such node exists"""
    pass


def has_node(n):
    """True if ndoe n is contained in graph, otherwise False"""
    pass


def neighbors(n):
    """Returns list of all nodes connected to n by edges
       raises an error if n is not in g"""
    pass


def adjacent(n1, n2):
    """returns True if there is an edge connecting n1 and n2
       False if not. Raises an error if either the supplied
       nodes not in G"""
    pass
