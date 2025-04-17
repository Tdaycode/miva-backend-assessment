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




### 2. Alternate Min-Max Rearrangement

Modify a given array of integers so that the first element is the smallest, the second is the largest, the third is the second-smallest, the fourth is the second-largest, and so on.

#### Constraints:

- The input variable `arr` is a list of integers.
- The length of `arr` can be any non-negative integer.
- The elements in `arr` can be positive, negative, or zero.
- There are no specific constraints on the range of values for the elements in `arr`.

#### Examples:

- **Test Case 1:**
  ```
  Input: [13, 7, 8, 3, 2, 10, 15, -1]
  Output: [-1, 15, 2, 13, 3, 10, 7, 8]
  Description: This test case has a mix of positive and negative integers, which tests the function’s ability to sort and interleave them according to the problem's requirements.
  ```

- **Test Case 2:**
  ```
  Input: [-5, -12, -1, 7, 14, -7, 3, 6]
  Output: [-12, 14, -7, 7, -5, 6, -1, 3]
  Description: This case with both negative and positive integers challenges the algorithm to handle interleaving in a more complex array with negative values.
  ```

- **Test Case 3:**
  ```
  Input: [3, 6, 9, -10, -5, -2, 0, 8]
  Output: [-10, 9, -5, 8, -2, 6, 0, 3]
  Description: This test case includes negative numbers, positive numbers, and a zero, providing a robust test of the sorting and interleaving mechanism.
  ```