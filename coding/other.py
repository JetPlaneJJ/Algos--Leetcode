from typing import List
import math

#--------------------------------------------------------------------------------------------------
# Complete the getSequenceSum function below.
# Given integers i,j,k, find the total sum from numbers i up to j, and back down to k inclusive.
# Ex: getSequenceSum(0, 2, -1) = 0 + 1 + 2 + 1 + 0 + -1 = 3
def getSequenceSum(i, j, k):
    # total_sum = sum(range(i, j+1)) + sum(reversed(range(k, j))) # short/correct but not ideal...
    
    # more ideal: if start to mid overlaps with mid to end, then use it again
    total_sum = sum(range(i, j+1))  # add from start to mid inclusive
    if k == i:
        total_sum = ((total_sum - j) * 2) + j
    elif k < i:
        total_sum = ((total_sum - j) * 2) + j + sum(reversed(range(k, i)))
    else:
        total_sum += sum(reversed(range(k, j)))
    return total_sum # O(k - i)

#--------------------------------------------------------------------------------------------------
# Palindrome O(N) of numbers, no string conversion. Returns true if x is a palindrome.
def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    if x == 0:
        return True
    num_digits = int(math.log10(x) + 1)
    for i in range(0, num_digits//2 + 1): # compare starts and ends digits
        if (x // 10**i) % 10 != (x // 10**(num_digits - 1 - i)) % 10:
            return False
    return True

#--------------------------------------------------------------------------------------------------
# Given a randomly sorted array of integers, find three numbers that sum up to 0.
# i != j != k and nums[i] + nums[j] + nums[k] == 0
# Returns a list of all triplet values that meet the above conditions. The returned lists must
# contain values sorted ascending, no duplicates.
# Ex: nums = [-1,0,1,2,-1,-4]  --> Output: [[-1,-1,2],[-1,0,1]]
def threeSum(nums: List[int]) -> List[List[int]]:
    solutions = set() # space O(N)
    list_size = len(nums)
    if list_size < 3: # there are no triplets
        return solutions
    
    search_list = {} # space O(N)
    for index in range(0, list_size): # O(N)
        search_list[nums[index]] = index # values and their index in original array

    for x in range(0, list_size - 2): # O(N^2)
        for y in range(x + 1, list_size - 1):
            sum_negate = -(nums[x] + nums[y]) # negate the 1st two
            result_index = search_list.get(sum_negate) # get the negation if it exists
            if (result_index is not None and result_index != x and result_index != y):
                s = (nums[x], nums[y], sum_negate)
                new_solution = tuple(sorted(s))
                solutions.add(new_solution)

    return solutions # Time = O(N^2), Space = O(N)