# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


def level_order(root):
    """
    Problem:
    Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by
    level).

    :type root: Node
    :rtype: List[List[int]]

    Solution: Queue up all the nodes at the current level and handle their traversal, then start a new queue with the
    next level, i.e. do BFS starting from the root until all nodes have been touched.
    """

    if not root:
        return []

    levels = []
    current_queue = [root]

    while current_queue:

        level = []
        next_queue = []

        for node in current_queue:
            level.append(node.val)
            if node.children:
                for child in node.children:
                    next_queue.append(child)

        levels.append(level)
        current_queue = next_queue

    return levels
