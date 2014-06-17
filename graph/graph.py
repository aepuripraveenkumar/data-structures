

class Node(object):

    def __init__(self, value):
        self.value = value


class Edge(object):

    def __init__(self, node1, node2):
        self.nodes = (node1, node2)


class Graph(object):

    def __init__(self):
        self.nodelist = []
        self.edgelist = []

    def add_node(self, *args):
        for arg in args:
            self.nodelist.append(arg)

    def nodes(self):
        return self.nodelist

    def has_node(self, node_value):
        for node in self.nodelist:
            if node.value == node_value:
                return True
        return False
