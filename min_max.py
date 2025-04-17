# 2.Alternate Min-Max Rearrangement

# Modify a given array of integers so that the first element is the smallest, the second is the
# largest, the third is the second-smallest, the fourth is the second-largest, and so on.
# Constraints:
# The input variable arr is a list of integers.
# The length of arr can be any non-negative integer.
# The elements in arr can be positive, negative, or zero.
# There are no specific constraints on the range of values for the elements in arr.

# Approaching the question
# There are many approach to the question, but I will be using the two-pointer approach, because of the following reasons:
# 1. It is a simple and efficient approach.
# 2. It is easy to implement and understand.
# 3. It is memory efficient.
# The time complexity of the approach is O(nlogn) due to the sorting step.
# The space complexity of the approach is O(1) since we are not using any additional space.

def alternate_min_max(arr):
    """
    Modify a given array of integers so that the first element is the smallest, the second is the largest, the third is the second-smallest, the fourth is the second-largest, and so on.
    
    :param arr: List[int] representing the input array of integers.
    :return: List[int] representing the modified array with alternate min-max rearrangement.
    """
    # Sort the array in ascending order
    arr.sort()
    # Initialize an empty list to store the result
    result = []
    # Initialize two pointers, one at the start and one at the end of the array
    left, right = 0, len(arr) - 1

    # Use a while loop to alternate between the smallest and largest elements
    while left <= right:
        # Append the smallest element
        result.append(arr[left])
        # Move the left pointer to the right
        left += 1    
        if left <= right: 
            # Append the largest element
            result.append(arr[right])
            # Move the right pointer to the left    
            right -= 1  
    return result
print(alternate_min_max([]))
print(alternate_min_max([-5, -12, -1, 7, 14, -7, 3, 6]))
print(alternate_min_max([3, 6, 9, -10, -5, -2, 0, 8]))

    