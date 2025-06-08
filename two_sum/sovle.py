from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store number and its corresponding index
        num_to_index = {}
        for index, num in enumerate(nums):
            # Calculate the complement
            complement = target - num
            # Check if the complement (needed number) exists in the dictionary
            if complement in num_to_index:
                return [num_to_index[complement], index]  # Found the solution
            # If not found, store the current number with its index
        return []  # In a valid input, we shouldn't reach here since there is exactly one solution
            num_to_index[num] = index

# Example usage
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
print(solution.twoSum([3, 2, 4], 6))       # Output: [1, 2]
print(solution.twoSum([3, 3], 6))          # Output: [0, 1]
