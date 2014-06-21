import pytest
from guido_graph import Graph
from queue import Node, Queue


def test_add_node():
    graph1 = Graph()
    graph1.add_node('A')
    graph1.add_node('B')
    assert graph1.nodes() == ['A', 'B']


def test_add_existing_node():
    graph1 = Graph()
    graph1.add_node('A')
    graph1.add_node('A')
    assert graph1.nodes() == ['A']


def test_add_edge():
    graph1 = Graph()
    graph1.add_node('A')
    graph1.add_node('B')
    graph1.add_edge('A', 'B')
    assert graph1.edges() == [('A', 'B')]


def test_add_edge_no_node():
    graph1 = Graph()
    graph1.add_edge('A', 'B')
    assert graph1.edges() == [('A', 'B')]
    assert graph1.nodes() == ['A', 'B']


def test_del_node():
    graph1 = Graph()
    graph1.add_node('A')
    graph1.add_node('B')
    assert graph1.nodes() == ['A', 'B']
    graph1.del_node('B')
    assert graph1.nodes() == ['A']


def test_del_node_with_edges():
    graph1 = Graph()
    graph1.add_node('A')
    graph1.add_node('B')
    graph1.add_node('C')
    graph1.add_edge('A', 'B')
    graph1.add_edge('C', 'A')
    graph1.del_node('A')
    assert len(graph1.edges()) == 0
    assert graph1.has_node('B')
    assert graph1.has_node('C')


def test_del_ghost_node():
    graph1 = Graph()
    with pytest.raises(ValueError):
        graph1.del_node('A')


def test_neighbors_positive():
    graph1 = Graph()
    graph1.add_node('A')
    graph1.add_node('B')
    graph1.add_node('C')
    graph1.add_edge('A', 'B')
    graph1.add_edge('C', 'A')
    assert graph1.neighbors('A') == ['B']


def test_neighbors_negative():
    graph1 = Graph()
    graph1.add_node('A')
    graph1.add_node('B')
    graph1.add_node('C')
    with pytest.raises(ValueError):
        graph1.neighbors('D')


def test_adjacent_positive():
    graph1 = Graph()
    graph1.add_node('A')
    graph1.add_node('B')
    graph1.add_node('C')
    graph1.add_edge('A', 'B')
    graph1.add_edge('C', 'A')
    assert graph1.adjacent('A', 'B')


def test_adjacent_negative():
    graph1 = Graph()
    graph1.add_node('A')
    graph1.add_node('B')
    graph1.add_node('C')
    graph1.add_edge('A', 'B')
    graph1.add_edge('C', 'A')
    assert graph1.adjacent('B', 'C') is False


def test_adjacent_error():
    graph1 = Graph()
    graph1.add_node('A')
    graph1.add_node('B')
    graph1.add_node('C')
    graph1.add_edge('A', 'B')
    graph1.add_edge('C', 'A')
    with pytest.raises(ValueError):
        graph1.adjacent('D', 'C')


def test_add_to_queue():
    graph1 = Graph()
    graph1.add_node('A')
    graph1.add_node('B')
    graph1.add_node('C')
    graph1.add_edge('A', 'B')
    graph1.add_edge('A', 'C')
    graph1.breadth_first_traversal('A')
    assert graph1.queue.head.node_name == ['B', 'C']
