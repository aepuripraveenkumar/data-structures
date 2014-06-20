import pytest
from guido_graph import graph
from guido_graph import nodes
from guido_graph import edges
from guido_graph import add_node
from guido_graph import add_edge


# @pytest.fixture(scope='function'):
#     pass


def test_add_node():
    add_node('A')
    add_node('B')
    assert nodes() == ['A', 'B']


def test_add_edge():
    add_node('A')
    add_node('B')
    add_edge('A', 'B')
    assert edges() == [('A', 'B')]
