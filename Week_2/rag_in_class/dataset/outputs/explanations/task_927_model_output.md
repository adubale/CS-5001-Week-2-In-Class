# Model output for task_927

## Model
- devstral-small-2:24b-cloud

## Original Code:

class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None
def max_height(node): 
	if node is None: 
		return 0 ; 
	else : 
		left_height = max_height(node.left) 
		right_height = max_height(node.right) 
		if (left_height > right_height): 
			return left_height+1
		else: 
			return right_height+1

## Refactored Code:

```python
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
```

- Preserved the exact same public API (Node class and max_height function)
- Maintained the same recursive algorithm and base case handling
- Simplified the return logic using max() instead of if-else
- Added a clear docstring explaining the function's purpose and behavior
- Kept all variable names meaningful and consistent
- Preserved the exact same behavior for all edge cases (None input, empty tree, etc.)
- Maintained the same time and space complexity (O(n) time, O(h) space where h is tree height)
- No changes to the Node class structure or initialization
- All test cases should pass without modification
