# Example from https://www.python.org/doc/essays/graphs/
"""graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}"""


class Graph(object):
    def __init__(self):
        self.graph = {}

    def nodes(self):
        """return list of all nodes in graph"""
        return self.graph.keys()

    def edges(self):
        """return list of all edges in graph"""
        return [(i, e) for i in self.graph.keys() for e in self.graph[i]]

    def add_node(self, n):
        """adds new node 'n' to graph"""
        if n not in self.graph.keys():
            self.graph[n] = []

    def add_edge(self, n1, n2):
        """"adds new edge to graph connecting n1 and n2
            if either n1 or n2 are not already in graph, adds them"""
        nodes = self.graph.keys()
        if n1 not in nodes:
            self.graph[n1] = []
        if n2 not in nodes:
            self.graph[n2] = []
        self.graph[n1].append(n2)

    def del_node(self, n):
        """deletes node n from graph
           raises error if no such node exists"""
        if n in self.graph.keys():
            self.graph.remove(n)
        else:
            raise ValueError

    def del_edge(self, n1, n2):
        """deletes edge containing n1 and n2 from graph
           raises error if no such node exists"""
        pass

    def has_node(self, n):
        """True if ndoe n is contained in graph, otherwise False"""
        pass

    def neighbors(self, n):
        """Returns list of all nodes connected to n by edges
           raises an error if n is not in g"""
        pass

    def adjacent(self, n1, n2):
        """returns True if there is an edge connecting n1 and n2
           False if not. Raises an error if either the supplied
           nodes not in G"""
        pass
