# miva-backend-assessment
miva-backend-assessment

# Plus One Problem

## Problem Statement
You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the i-th digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading `0`s.

You need to increment the large integer by one and return the resulting array of digits.

### Examples

**Example 1:**
```
Input: digits = [1, 2, 3]
Output: [1, 2, 4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1, 2, 4].
```

**Example 2:**
```
Input: digits = [4, 3, 2, 1]
Output: [4, 3, 2, 2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4, 3, 2, 2].
```

**Example 3:**
```
Input: digits = [9]
Output: [1, 0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1, 0].
```

### Constraints
- `1 <= digits.length <= 100`
- `0 <= digits[i] <= 9`
- The input array does not contain any leading `0`s.

---

## Approaches to Solution

### **Approach 1: Convert, Increment, and Split**

1. **Description**:
   - Convert the array of digits into an integer.
   - Increment the integer by 1.
   - Convert the resulting integer back into an array of digits.

2. **Advantages**:
   - Straightforward and easy to implement.

3. **Disadvantages**:
   - Inefficient for larger datasets due to the overhead of converting between integers and strings.
   - Higher space complexity because of intermediate representations (e.g., strings).

4. **Complexity**:
   - **Time Complexity**: O(n), where `n` is the number of digits in the array.
   - **Space Complexity**: O(n), due to the intermediate string and integer representations.

### **Approach 2: Basic Math Method**

1. **Description**:
   - Traverse the array of digits from right to left.
   - Increment the last digit if it is less than 9. If it is 9, set it to 0 and propagate the carry to the next digit.
   - If all digits are 9 (e.g., `[9, 9, 9]`), add a new leading `1` to the array.

2. **Advantages**:
   - Efficient and uses constant extra space.
   - Mimics how addition is performed manually, making it intuitive.

3. **Disadvantages**:
   - Slightly more complex implementation due to the need for carry propagation.

4. **Complexity**:
   - **Time Complexity**: O(n), where `n` is the number of digits in the array.
   - **Space Complexity**: O(1), since the array is modified in place (except in the case of leading `1` addition).

5. **Implementation**:

```python
def plus_one(digits):
    """
    Increment the given array of digits by one.
    
    :param digits: List[int] representing a large integer.
    :return: List[int] representing the incremented large integer.
    """
    # Traverse the array from right to left
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            # Increment the current digit if it's less than 9
            digits[i] += 1
            return digits
        else:
            # Set the current digit to 0 and continue to the next digit
            digits[i] = 0
    
    # If all digits are 9, add a new leading 1
    return [1] + digits

# Example Usage
print(plus_one([1, 2, 3]))  # Output: [1, 2, 4]
print(plus_one([4, 3, 2, 1]))  # Output: [4, 3, 2, 2]
print(plus_one([9]))  # Output: [1, 0]
```

---

## Final Thoughts

Given the constraints (`1 <= digits.length <= 100`), the **Basic Math approach** is optimal due to its constant space complexity and efficient traversal. The convert-increment-split method is easier to implement but less efficient for larger inputs.
