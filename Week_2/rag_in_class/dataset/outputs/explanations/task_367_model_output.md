# Model output for task_367

## Model
- devstral-small-2:24b-cloud

## Original Code:

class Node: 
	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None
def get_height(root): 
	if root is None: 
		return 0
	return max(get_height(root.left), get_height(root.right)) + 1
def is_tree_balanced(root): 
	if root is None: 
		return True
	lh = get_height(root.left) 
	rh = get_height(root.right) 
	if (abs(lh - rh) <= 1) and is_tree_balanced( 
	root.left) is True and is_tree_balanced( root.right) is True: 
		return True
	return False

## Refactored Code:

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def get_height(root):
    if root is None:
        return 0
    return max(get_height(root.left), get_height(root.right)) + 1

def is_tree_balanced(root):
    if root is None:
        return True
    left_height = get_height(root.left)
    right_height = get_height(root.right)
    return (abs(left_height - right_height) <= 1) and \
           is_tree_balanced(root.left) and \
           is_tree_balanced(root.right)
```

- Simplified the boolean logic in `is_tree_balanced` by removing redundant `is True` checks
- Improved variable naming for clarity (e.g., `lh` → `left_height`, `rh` → `right_height`)
- Maintained exact behavior as validated by the provided tests
- Preserved the recursive structure for height calculation and balance checking
- Ensured all edge cases (empty tree, single node) are handled correctly
- Kept the original function signatures and return types unchanged
- Used consistent indentation and spacing for better readability
- Maintained the same mathematical logic for height calculation and balance verification
