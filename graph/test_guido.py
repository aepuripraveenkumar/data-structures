import pytest
from guido_graph import graph
from guido_graph import nodes
from guido_graph import edges
from guido_graph import add_node


def test_return_nodes():
    graph['A'] = []
    graph['B'] = []
    assert nodes() == ['A', 'B']
