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
    assert graph_init[0].nodelist == [graph_init[1], graph_init[2],
                                      graph_init[3]]


def test_has_node(graph_init):
    assert graph_init[0].has_node("William") is True
    assert graph_init[0].has_node("Fred") is False


def test_add_edge(graph_init):
    graph_init[0].add_edge(graph_init[1], graph_init[2])
    assert len(graph_init[0].edgelist) == 4


def test_edge_list(graph_init):
    assert len(graph_init[0].edges()) == 3


def test_delete_edge(graph_init):
    graph_init[0].del_edge(graph_init[1], graph_init[2])
    assert len(graph_init[0].edges()) == 2


def test_delete_edge_error(graph_init):
    graph_init[0].del_edge(graph_init[1], graph_init[2])
    with pytest.raises(ValueError):
        graph_init[0].del_edge(graph_init[1], graph_init[2])


def test_delete_node(graph_init):
    graph_init[0].del_node(graph_init[1])
    assert graph_init[0].has_node(graph_init[1]) is False
    assert graph_init[0].edgelist[0].nodes[0] == graph_init[2]
    assert graph_init[0].edgelist[0].nodes[1] == graph_init[3]
    with pytest.raises(ValueError):
        graph_init[0].del_node(graph_init[1])


def test_adjacent(graph_init):
    node5 = Node("What?")
    graph_init[0].del_edge(graph_init[1], graph_init[2])
    assert graph_init[0].adjacent(graph_init[2], graph_init[3]) is True
    assert graph_init[0].adjacent(graph_init[1], graph_init[2]) is False
    with pytest.raises(ValueError):
        graph_init[0].adjacent(graph_init[1], node5)
