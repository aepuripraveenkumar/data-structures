import guido_graph


def dijkstra(graph, source, target):
    dist = {source: 0}
    path = {}

    nodes = set(graph.nodes())
    for node in nodes:
        if node != source:
            dist[node] = float('inf')
            path[node] = None

    while nodes:
        min_node = None
        for node in nodes:
            if node in dist:
                if min_node is None:
                    min_node = node
                elif dist[node] < dist[min_node]:
                    min_node = node
        if min_node is None:
            break
        nodes.remove(min_node)
        current_distance = dist[min_node]

        for neighbor in graph.edges(min_node):
            distance = current_distance + graph.graph[min_node][neighbor]
            if neighbor not in dist or distance < dist[neighbor]:
                dist[neighbor] = distance
                path[neighbor] = min_node

    s_path = []
    current = target
    while current in path:
        s_path.append(current)
        current = path[current]
    s_path.append(source)
    s_path.reverse()
    return s_path, dist[target]
