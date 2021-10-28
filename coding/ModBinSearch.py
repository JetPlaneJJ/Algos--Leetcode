from typing import List
import math
#--------------------------------------------------------------------------------------------------
class ModifiedBinarySearch:
# 3) Modified Binary Search: tackles trickier "find element" problems similar to regular Bin S.
# Note: Binary Search takes O(log(N)) runtime.
# Usage: Find the _____ element in a ROTATED and Sorted array”

    # Ex: Find the minimum value in a rotated and sorted array
    # Array = length n, rotated however many times. All integers are unique, can be (-).
    # Example arrays: [2, 3, 4, 5, 0, 1], [0, 1, 2], [1, -1, 0]
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while (start < end):
            mid = math.floor((end + start)/2) # find mid position, see if min
            if (nums[mid] > nums[end]):
                start = mid + 1 # the right half was actually smaller, shift to the right
            else:
                end = mid
        return nums[start]

#--------------------------------------------------------------------------------------------------
    # Returns the index of a target value given a ROTATED and sorted array of unique numbers.
    # Returns -1 if not found.
    # ex: [4,5,6,7,0,1,2], target = 0. [4,5,6,1,2], target = 4. [3,4,1,2], target = 4.
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while (start <= end):
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[start]: # is sorted on its left
                # usually shift right if sorted all the way
                # special case: the left was sorted but is still bigger than right
                if nums[mid] < target or nums[start] > target: 
                    start = mid + 1 # shift right
                else:
                    end = mid - 1
            else: # not sorted on the left
                if nums[mid] > target or nums[end] < target:
                    end = mid - 1
                else:
                    start = mid + 1
        return -1
