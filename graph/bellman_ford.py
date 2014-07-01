

INF = float('Inf')


def bellman_ford_algo(graph, root_node, final_node):
    """
    Bellman ford shortest path algorithm, checks if graph is negative
    Checks every edge at each iteration
    """

    distances = {}
    has_cycle = False

    # initialize every node to infinity except the root node
    for node in graph.nodes():
        distances[node] = 0 if node == root_node else INF

    # weight = graph.graph[edge[0]][edge[1]]
    # repeat nodes-1 times
    for i in range(1, len(graph.nodes())):
        # iterate over every edge
        for edge in graph.edges():
                # n1 is edge[0], n2 is edge[1]
                # if edge can be relaxed, relax it
                if distances[edge[1]] > distances[edge[0]] + graph.graph[edge[0]][edge[1]]:
                    distances[edge[1]] = distances[edge[0]] + graph.graph[edge[0]][edge[1]]

    # if a node can still be relaxed, there is a negative cycle
    # therefore assumption is false, cant be solved
    for edge in graph.edges():
            if distances[edge[1]] > distances[edge[0]] + graph.graph[edge[0]][edge[1]]:
                has_cycle = True

    return has_cycle, distances[final_node]
