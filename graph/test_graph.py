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
