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
        node: The root node of the binary tree (or None for an empty tree).

    Returns:
        int: The maximum height of the tree, where an empty tree has height 0.
    """
    if node is None:
        return 0
    left_height = max_height(node.left)
    right_height = max_height(node.right)
    return max(left_height, right_height) + 1
```

- Preserved the exact behavior of the original implementation, including handling of None input
- Simplified the conditional logic using `max()` function without changing behavior
- Added docstring to explain the function's purpose and behavior
- Maintained the same function signature and return type
- Kept the recursive approach with identical base case and recursive cases
- Preserved the height calculation formula (max child height + 1)
- No changes to the Node class structure or initialization
- All test cases should pass without modification
