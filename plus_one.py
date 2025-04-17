# 1. Plus One

# You are given a large integer represented as an integer array digits, where each digits[i] is the
# i
# th digit of the integer. The digits are ordered from most significant to least significant in
# left-to-right order. The large integer does not contain any leading 0's.
# Increment the large integer by one and return the resulting array of digits.

# print(plus_one([1, 2, 3]))  # Output: [1, 2, 4]
# print(plus_one([4, 3, 2, 1]))  # Output: [4, 3, 2, 2]
# print(plus_one([9]))  # Output: [1, 0]

# Approaching the question
# There are two approaches to this question:
# 1. Convert the array to an integer, increment it by one, and then convert it back to an array.
# 2. Iterate through the array from right to left and increment the last digit by one if it is less than 9 else loop through the array and increment the next digit by one.

# Approach 1
# The first approach is straight forward and easy to implement, and understand. But there is a bottle neck in the approach especially when we are dealing with large data set, it takes up more memory because we are creating a new array.
# This makes the space complexity of the approach O(n) where n is the length of the array. And the time complexity of the approach is also O(n) where n is the length of the array.

# Approach 2
# The second approach is more efficient and less memory consuming. It uses a for loop to iterate through the array from right to left and increment the last digit by one if it is less than 9 else loop through the array and increment the next digit by one.
# This makes the space complexity of the approach O(1) and the time complexity of the approach is also O(n) where n is the length of the array.
# In fact the time complexity can be said to be constant time  O(1) in a situation when the last digit is always less than 9.
# And since our array is mutable, we can modify the array in place and return it. Furthermore I decided to go for this approach because the constraints of the question says our digits can be up to 100 which is a large data set.
# In summary, this approach follow the basic mathematics method of addition  22+ 1 where we add one to the right most digit and if the right most digit is 9, we add one to the next digit and so on.
# Implementation

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
            
    

print(plus_one([1, 2, 3]))
print(plus_one([4, 3, 2, 1]))
print(plus_one([9]))
