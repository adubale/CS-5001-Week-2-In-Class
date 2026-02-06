class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def get_height(root):
    """Calculate the height of a binary tree rooted at `root`.

    Args:
        root: The root node of the tree (or None for empty tree).

    Returns:
        int: The height of the tree (0 for empty tree).
    """
    if root is None:
        return 0
    return max(get_height(root.left), get_height(root.right)) + 1

def is_tree_balanced(root):
    """Check if a binary tree is balanced.

    A tree is balanced if:
    1. The heights of the two child subtrees of any node differ by no more than 1.
    2. Both child subtrees are balanced.

    Args:
        root: The root node of the tree (or None for empty tree).

    Returns:
        bool: True if the tree is balanced, False otherwise.
    """
    if root is None:
        return True

    left_height = get_height(root.left)
    right_height = get_height(root.right)

    # Check if current node is balanced and both subtrees are balanced
    return (abs(left_height - right_height) <= 1 and
            is_tree_balanced(root.left) and
            is_tree_balanced(root.right))
