from guido_graph import Graph
from bellman_ford import bellman_ford_algo


def test_weight_values():
    graph1 = Graph()
    graph1.add_node('A')
    graph1.add_node('B')
    graph1.add_node('C')
    graph1.add_edge('A', 'B', 1)
    graph1.add_edge('A', 'C', 25)
    assert graph1.graph['A']['B'] == 1
    assert graph1.graph['A']['C'] == 25


def test_bellman():
    graph1 = Graph()
    graph1.add_node('A')
    graph1.add_node('B')
    graph1.add_node('C')
    graph1.add_node('D')
    graph1.add_edge('A', 'B', 1)
    graph1.add_edge('A', 'C', 25)
    graph1.add_edge('B', 'C', 5)
    graph1.add_edge('B', 'D', 55)
    graph1.add_edge('C', 'D', 33)
    graph1.add_node('B', 'C', 100)
    assert graph1.graph['A']['B'] == 1
    assert graph1.graph['A']['C'] == 25