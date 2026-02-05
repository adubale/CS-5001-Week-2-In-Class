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
    if node is None:
        return 0
    left_height = max_height(node.left)
    right_height = max_height(node.right)
    return max(left_height, right_height) + 1
```

- Simplified the conditional logic in `max_height` by using `max()` function directly
- Maintained the exact same behavior and return type
- Preserved the recursive structure for tree traversal
- Kept the edge case handling for `None` nodes
- Ensured the function still returns the correct height calculation
- Maintained the same function signature and name
- Improved readability by reducing nested conditionals
