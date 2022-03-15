from typing import List

# --------------------------------------------------------------------------------------------------
# Dynamic Programming is an optimized linear form of solutions to some recursive problems.
# If the recursive solution has repeated calls for same inputs, DP is the optimization.
class DynamicProgramming:

# --------------------------------------------------------------------------------------------------
    # Given an integer array nums, find the contiguous subarray (containing at least one number) 
    # which has the largest sum and return its sum. Your answer must NOT use recursion and should
    # run in linear time with O(1) extra space.
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        
        curr_max = nums[0] # local maximum
        best_max = nums[0] # absolute maximum
        
        for i in range(1, len(nums)):
            # reset if new number made sum worse
            curr_max = max(nums[i], curr_max + nums[i]) 
            # update absolute max with best local max seen so far
            best_max = max(best_max, curr_max)
            
        return best_max
