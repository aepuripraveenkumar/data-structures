import pytest
from guido_graph import Graph


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


def test_del_node():
    graph1 = Graph()
    graph1.add_node('A')
    graph1.add_node('B')
    graph1.del_node('B')
    assert graph1.nodes() == ['A']


def test_del_ghost_node():
    graph1 = Graph()
    with pytest.raises(ValueError):
        graph1.del_node('A')
