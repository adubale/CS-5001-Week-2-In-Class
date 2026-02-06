class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def max_height(node):
    """Calculate the maximum height of a binary tree rooted at the given node.

    Args:
        node: The root node of the binary tree. Can be None for an empty tree.

    Returns:
        int: The maximum height of the tree. Returns 0 for an empty tree.
    """
    if node is None:
        return 0
    left_height = max_height(node.left)
    right_height = max_height(node.right)
    return max(left_height, right_height) + 1
