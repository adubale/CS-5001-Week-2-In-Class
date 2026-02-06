class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def max_height(node):
    """Calculate the maximum height of a binary tree rooted at the given node.

    Args:
        node: The root node of the binary tree (or None for an empty tree).

    Returns:
        int: The maximum height of the tree, where an empty tree has height 0.
    """
    if node is None:
        return 0
    left_height = max_height(node.left)
    right_height = max_height(node.right)
    return max(left_height, right_height) + 1
