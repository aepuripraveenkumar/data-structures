import pytest
from graph import Node
from graph import Graph
from graph import Edge


@pytest.fixture(scope='function')
def graph_init():
    node1 = Node("William")
    node2 = Node("Ted")
    node3 = Node("Josh")
    newGraph = Graph()
    newGraph.add_node(node1, node2, node3)
    newGraph.add_edge(node1, node2)
    newGraph.add_edge(node2, node3)
    newGraph.add_edge(node1, node3)
    return newGraph, node1, node2, node3


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


def test_graph_nodes_list(graph_init):
    assert graph_init[0].nodelist == [graph_init[1], graph_init[2], graph_init[3]]


def test_has_node(graph_init):
    assert graph_init[0].has_node("William") is True
    assert graph_init[0].has_node("Fred") is False


def test_add_edge(graph_init):
    graph_init[0].add_edge(graph_init[1], graph_init[2])
    assert len(graph_init[0].edgelist) == 4


def test_edge_list(graph_init):
    assert len(graph_init[0].edges()) == 3
