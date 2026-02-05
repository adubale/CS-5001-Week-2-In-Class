# Model output for task_641

## Model
- devstral-small-2:24b-cloud

## Original Code:

def is_nonagonal(n): 
	return int(n * (7 * n - 5) / 2) 

## Refactored Code:

```python
def is_nonagonal(n):
    return int(n * (7 * n - 5) / 2)
```

- The function `is_nonagonal` calculates the nth nonagonal number using the exact formula provided in the problem statement.
- The formula `n * (7 * n - 5) / 2` is implemented precisely to ensure correct results for all integer inputs.
- The result is cast to an integer to match the expected output type, as nonagonal numbers are always integers.
- Edge cases such as `n = 0` and negative values are handled naturally by the formula, returning `0` and negative values respectively.
- The function is concise and directly maps to the mathematical definition, ensuring clarity and maintainability.
- No intermediate validations are needed as the formula is mathematically sound and the input is assumed to be an integer.
- The function preserves the exact behavior required by the tests, including precision and return type.
