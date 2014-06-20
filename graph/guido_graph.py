
class Graph(object):
    def __init__(self):
        self.graph = {}

    def nodes(self):
        """return list of all nodes in graph"""
        return self.graph.keys()

    def edges(self):
        """return list of all edges in graph"""
        return [(i, e) for i in self.nodes() for e in self.graph[i]]

    def add_node(self, n):
        """adds new node 'n' to graph"""
        if n not in self.nodes():
            self.graph[n] = []

    def add_edge(self, n1, n2):
        """"adds new edge to graph connecting n1 and n2
            if either n1 or n2 are not already in graph, adds them"""
        if n1 not in self.nodes():
            self.graph[n1] = []
        if n2 not in self.nodes():
            self.graph[n2] = []
        self.graph[n1].append(n2)

    def del_node(self, n):
        """deletes node n from graph
           raises error if no such node exists"""
        if n in self.nodes():
            del self.graph[n]
            for i in self.nodes():
                if n in self.graph[i]:
                    self.graph[i].remove(n)
        else:
            raise ValueError

    def del_edge(self, n1, n2):
        """deletes edge containing n1 and n2 from graph
           raises error if no such node exists"""
        if n1 in self.graph.keys():
            self.graph[n1].pop(n2)
        else:
            raise ValueError

    def has_node(self, n):
        """True if node n is contained in graph, otherwise False"""
        if n in self.graph.keys():
            return True
        else:
            return False

    def neighbors(self, n):
        """Returns list of all nodes connected to n by edges
           raises an error if n is not in g"""
        if self.has_node(n):
            return [neighbor for neighbor in self.graph[n]]
        else:
            raise ValueError

    def adjacent(self, n1, n2):
        """returns True if there is an edge connecting n1 and n2
           False if not. Raises an error if either the supplied
           nodes not in G"""
        if self.has_node(n1) and self.has_node(n2):
            if n2 in self.neighbors(n1) or n1 in self.neighbors(n2):
                return True
            else:
                return False
        else:
            raise ValueError
