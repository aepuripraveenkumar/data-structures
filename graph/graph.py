

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

    def edges(self):
        return self.edgelist

    def has_node(self, node_value):
        for node in self.nodelist:
            if node.value == node_value:
                return True
        return False

    def add_edge(self, node1, node2):
        if not self.has_node(node1.value):
            node1 = Node(node1.value)
            self.add_node(node1)
        if not self.has_node(node2.value):
            node2 = Node(node2.value)
            self.add_node(node2)
        self.edgelist.append(Edge(node1, node2))

    def del_edge(self, node1, node2):
        removed = False
        for edge in self.edgelist:
            if node1 in edge.nodes and node2 in edge.nodes:
                self.edgelist.remove(edge)
                removed = True
                break
        if not removed:
            raise ValueError

    def del_node(self, node1):
        removed = False
        for item in self.nodelist:
            if item.value == node1.value:
                self.nodelist.remove(item)
                removed = True
                break
        if removed:
            for item in self.edgelist:
                if node1 in item.nodes:
                    self.edgelist.remove(item)
        else:
            raise ValueError

    def adjacent(self, node1, node2):
        if not self.has_node(node1.value) or \
                not self.has_node(node2.value):
            raise ValueError
        for item in self.edgelist:
            if node1 in item.nodes and node2 in item.nodes:
                return True
        return False

    def neighbors(self, node1):
        n_list = []
        if not self.has_node(node1.value):
            raise ValueError
        for item in self.edgelist:
            if item.nodes[0] == node1:
                n_list.append(item.nodes[1])
            elif item.nodes[1] == node1:
                n_list.append(item.nodes[0])
        return n_list
