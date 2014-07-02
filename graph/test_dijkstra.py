from dijkstra import dijkstra
import guido_graph


def test_dkystra_1():
    graph1 = guido_graph.Graph()
    graph1.add_edge('A', 'B', 2)
    graph1.add_edge('A', 'C', 10)
    graph1.add_edge('C', 'F', 1)
    graph1.add_edge('B', 'D', 3)
    graph1.add_edge('D', 'E', 5)
    graph1.add_edge('E', 'F', 2)
    graph1.add_edge('B', 'F', 2)

    path, distance = dijkstra(graph1, 'A', 'F')

    assert path == ['A', 'B', 'F']
    assert distance == 4


def test_dkystra_2():
    graph1 = guido_graph.Graph()
    graph1.add_edge('A', 'B', 2)
    graph1.add_edge('A', 'C', 10)
    graph1.add_edge('C', 'F', 1)
    graph1.add_edge('B', 'D', 3)
    graph1.add_edge('D', 'E', 5)
    graph1.add_edge('E', 'F', 2)

    path, distance = dijkstra(graph1, 'A', 'F')

    assert path == ['A', 'C', 'F']
    assert distance == 11


def test_dkystra_3():
    graph1 = guido_graph.Graph()
    graph1.add_edge('A', 'B', 2)
    graph1.add_edge('A', 'C', 10)
    graph1.add_edge('C', 'F', 1)
    graph1.add_edge('B', 'D', 3)
    graph1.add_edge('D', 'E', 5)
    graph1.add_edge('E', 'F', 2)
    graph1.add_edge('D', 'C', 1)

    path, distance = dijkstra(graph1, 'A', 'F')

    assert path == ['A', 'B', 'D', 'C', 'F']
    assert distance == 7


def test_dkystra_4():
    graph1 = guido_graph.Graph()
    graph1.add_edge('A', 'B', 2)
    graph1.add_edge('A', 'C', 10)
    graph1.add_edge('C', 'F', 1)
    graph1.add_edge('B', 'D', 3)
    graph1.add_edge('D', 'E', 5)
    graph1.add_edge('E', 'F', 2)
    graph1.add_edge('D', 'C', 1)

    path, distance = dijkstra(graph1, 'B', 'C')

    assert path == ['B', 'D', 'C']
    assert distance == 4

def test_dykstra_5():
    graph1 = guido_graph.Graph()
    graph1.add_edge('A', 'B', 20)
    graph1.add_edge('A', 'C', 3)
    graph1.add_edge('C', 'D', 2)
    graph1.add_edge('C', 'E', 1)
    graph1.add_edge('D', 'F', 1)
    graph1.add_edge('F', 'B', 5)

    path, distance = dijkstra(graph1, 'A', 'B')
    assert path == ['A', 'C', 'D', 'F', 'B']
    assert distance == 11
