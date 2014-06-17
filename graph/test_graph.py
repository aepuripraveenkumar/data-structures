from graph import Node
from graph import Graph
from graph import Edge


def test_init_node():
    newNode = Node("Decatur")
    assert newNode.value == "Decatur"


def test_init_graph():
    newGraph = Graph()
    assert len(newGraph.nodelist) == 0
    assert len(newGraph.edgelist) == 0


def test_init_edge_w_nodes():
    node1 = Node("1st")
    node2 = Node("2nd")
    newEdge = Edge(node1, node2)
    assert len(newEdge.nodes) == 2
    assert newEdge.nodes[0].value == "1st"
    assert newEdge.nodes[1].value == "2nd"


def test_add_node():
    node1 = Node("William")
    newGraph = Graph()
    newGraph.add_node(node1)
    assert newGraph.nodelist[0].value == "William"
    assert len(newGraph.nodelist) == 1


def test_graph_nodes_list():
    node1 = Node("William")
    node2 = Node("Ted")
    node3 = Node("Josh")
    newGraph = Graph()
    newGraph.add_node(node1, node2, node3)
    assert newGraph.nodes() == [node1, node2, node3]


def test_has_node():
    newGraph = Graph()
    node1 = Node
