from typing import List
import math
#--------------------------------------------------------------------------------------------------
class SlidingWindows:
# 1) Sliding Windows: When to use? Find a "contiguous subarray", maximum sum/average...
#    Is O(N) because the whole array is traversed only once (no elements repeated).
# a) Fixed --> length is equal to X
# b) Dynamic --> find the "minimal length subarray"
    def findMaxAverage(self, nums: List[int], k: int) -> float: # find max average subarr size k
        n = len(nums)
        max_sum, curr_sum = -math.inf, 0
        start, end = 0, 0
        while end < n: # start moving the end position
          curr_sum += nums[end]
          if (end >= k - 1): # start moving the start (shifting window)
              max_sum = max(max_sum, curr_sum)
              curr_sum -= nums[start]
              start += 1
          end += 1
        return max_sum / k

    # Returns the minimum length subarray where the sum of subarray contents is 
    # >= given target. Return 0 if no such subarray exists.
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums)
        maxS, currS = 0, 0
        start, end = 0, 0 # end - start + 1 is current window length
        minLength = math.inf
        while (end < length):
            currS += nums[end] # keep growing right until can't anymore (>= the target)
            while (currS >= target): # keep shrinking from left until no longer >= target
                maxS = max(maxS, currS)
                minLength = min(minLength, end - start + 1)
                currS -= nums[start]
                start += 1
            end += 1
        if maxS < target: # edge case: if total sum in whole array < target
            return 0
        return minLength

    # Finds the area with the most water given a set of coordinates representing height.
    # Container can't be slanted (shortest height of the two).
    def maxArea(self, height: List[int]) -> int:
        start, end, bestArea = 0, len(height) - 1, 0
        while (start < end and end >= 0):
            currWidth = end - start
            currHeight = min(height[end], height[start])
            bestArea = max(bestArea, currHeight * currWidth)
            if (height[end] < height[start]): # always go for the taller one first
                end -= 1
            else:
                start += 1
        return bestArea