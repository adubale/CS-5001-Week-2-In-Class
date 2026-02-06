def kth_element(arr, n, k):
    """Return the k-th smallest element in the first n elements of arr after sorting.

    Args:
        arr: List of numbers to be sorted.
        n: Number of elements to consider from the start of arr.
        k: 1-based index of the element to return after sorting.

    Returns:
        The k-th smallest element in the first n elements of arr.
    """
    # Perform bubble sort on the first n elements
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr[k - 1]
