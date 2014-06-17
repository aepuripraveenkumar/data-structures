from graph import Node
from graph import Graph


def test_init_node():
    newNode = Node("Decatur")
    assert newNode.value == "Decatur"


def test_init_graph():
    newGraph = Graph()
    assert newGraph.nodelist is None
    assert newGraph.edgelist is None
