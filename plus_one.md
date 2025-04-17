# 1. Plus One

You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's. Increment the large integer by one and return the resulting array of digits.

## Examples

```python
print(plus_one([1, 2, 3]))  # Output: [1, 2, 4]
print(plus_one([4, 3, 2, 1]))  # Output: [4, 3, 2, 2]
print(plus_one([9]))  # Output: [1, 0]
```

## Approaching the Question

There are two approaches to this question:

### Approach 1

Convert the array to an integer, increment it by one, and then convert it back to an array.

- **Advantages**: Straightforward and easy to implement.
- **Drawbacks**: This approach can be memory-intensive, especially with large datasets, as it creates a new array.
- **Time Complexity**: O(n), where `n` is the length of the array.
- **Space Complexity**: O(n), due to the creation of a new array.

### Approach 2

Iterate through the array from right to left, incrementing the last digit by one if it is less than 9. If the digit is 9, set it to 0 and carry the addition to the next digit.

- **Advantages**: More efficient and memory-friendly. Since the array is modified in place, it avoids additional memory allocation.
- **Drawbacks**: Slightly more complex to implement compared to Approach 1.
- **Time Complexity**: O(n), where `n` is the length of the array. In cases where the last digit is not 9, it operates in O(1).
- **Space Complexity**: O(1), as it modifies the array in place.

### Why Choose Approach 2?

Given the constraints of the question (array length up to 100), Approach 2 is better suited for handling larger datasets efficiently. It follows basic arithmetic rules: start from the rightmost digit, add one, and handle carryovers if needed.

## Implementation

```python
def plus_one(digits):
    """
    Increment the given array of digits by one.
    
    :param digits: List[int] representing a large integer.
    :return: List[int] representing the incremented large integer.
    """
    # Traverse the array from right to left, the third -1 is to make sure it account for index 0 and doesn't go out of bounds.
    for i in range(len(digits) -1, -1, -1):

        if digits[i] < 9:
            # If the current digit is less than 9, increment it by 1 and return the array.
            digits[i] += 1
            return digits
        else:
            # If the current digit is 9, set it to 0 and continue to the next digit.
            digits[i] = 0
    
    # If all digits are 9, add a new digit 1 at the beginning of the array.
    return [1] + digits
            
    
```
