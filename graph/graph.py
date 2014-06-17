

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
