def all_paths_source_target(graph):
    """
    Source node is specified as node 0, target node is specified as node N-1.

    DFS for the target node beginning at the source node, maintaining the path;
    if the target node is reached, add that path to the list of valid paths. We
    are given that the graph is acyclic.

    :type graph: List[List[int]]
    :rtype: List[List[int]]
    """

    def dfs(node, path):
        if node == len(graph) - 1:
            paths.append(path + [node])
            return
        for child in graph[node]:
            dfs(child, path + [node])

    paths = []
    dfs(0, [])
    return paths
