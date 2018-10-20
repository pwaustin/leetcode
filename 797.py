def all_paths_source_target(graph):
    """
    Problem:
    Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in
    any order. The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all
    nodes j for which the edge (i, j) exists.

    :type graph: List[List[int]]
    :rtype: List[List[int]]

    Solution:
    DFS for the target node beginning at the source node, maintaining the path; if the target node is reached, add that
    path to the list of valid paths.
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
