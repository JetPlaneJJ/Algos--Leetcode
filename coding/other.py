from typing import List
import math

# --------------------------------------------------------------------------------------------------
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
    return total_sum  # O(k - i)

# --------------------------------------------------------------------------------------------------
# Palindrome O(N) of numbers, no string conversion. Returns true if x is a palindrome.
def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    if x == 0:
        return True
    num_digits = int(math.log10(x) + 1)
    for i in range(0, num_digits//2 + 1):  # compare start and end digits
        if (x // 10**i) % 10 != (x // 10**(num_digits - 1 - i)) % 10:
            return False
    return True # Solution is O(N) where N = number of digits

# --------------------------------------------------------------------------------------------------
# Given a randomly sorted array of integers, find three numbers that sum up to 0.
# i != j != k and nums[i] + nums[j] + nums[k] == 0
# Returns a list of all triplet values that meet the above conditions. The returned lists must
# contain values sorted ascending, no duplicates.
# Ex: nums = [-1,0,1,2,-1,-4]  --> Output: [[-1,-1,2],[-1,0,1]]
def threeSum(nums: List[int]) -> List[List[int]]:
    solutions = set()  # space O(N)
    list_size = len(nums)
    if list_size < 3:  # there are no triplets
        return solutions

    search_list = {}  # space O(N)
    for index in range(0, list_size):  # O(N)
        # values and their index in original array
        search_list[nums[index]] = index

    for x in range(0, list_size - 2):  # O(N^2)
        for y in range(x + 1, list_size - 1):
            sum_negate = -(nums[x] + nums[y])  # negate the 1st two
            # get the negation if it exists
            result_index = search_list.get(sum_negate)
            if (result_index is not None and result_index != x and result_index != y):
                s = (nums[x], nums[y], sum_negate)
                new_solution = tuple(sorted(s))
                solutions.add(new_solution)

    return solutions  # Time = O(N^2), Space = O(N)

# --------------------------------------------------------------------------------------------------
# You have n coins and you want to build a staircase with these coins.
# The staircase consists of k rows where the ith row has exactly i coins.
# The last row of the staircase may be incomplete.
# Given the integer n, return the number of complete rows of the staircase you will build.
def arrangeCoins(n: int) -> int:
    # O(n) solution -> BAD
    # Better solution: Time = (sqrt(n)) where python sqrt() function takes sqrt(n), Space = O(1)
    # Blocks: can get area of a block by doing length * length + 1 / 2, i * (i+1) / 2 = n
    # AKA find a square and halve that
    # _
    # __
    # ___ --> is half of

    #   ___ --> this, ex: 3 * (4) / 2 = 6
    #   ___
    # _  __
    # ___
    # ___
    # Then convert to i^2 + i - 2n = 0, find what i is and round down
    return math.floor(-0.5 + math.sqrt(0.25 + 2*n))
