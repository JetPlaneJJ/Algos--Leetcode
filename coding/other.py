from operator import xor
from typing import List
import math
from functools import reduce

# --------------------------------------------------------------------------------------------------
# Merged intervals variation.
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
# Easy TwoP variation
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
# 3SUM using a dictionary
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
# A hidden math question.
# You have n coins and you want to build a staircase with these coins.
# The staircase consists of k rows where the ith row has exactly i coins (ex: 3rd row = 3 coins)
# The last row of the staircase may be incomplete.
# Given the integer n, return the number of complete rows of the staircase you will build.
def arrangeCoins(n: int) -> int:
    # Linear time solution -> BAD
    # Better solution: Time = O(sqrt(n)) where python sqrt() function takes sqrt(n), Space = O(1)
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

# --------------------------------------------------------------------------------------------------
# The XOR trick. "Find the unique numbers in an array of duplicates".
# Must run in O(N), use only O(1) extra space. nums[i] can be negative or zero.

# Variation 1: find the ONE unique number, pretty easy!
# Given an integer array nums, in which exactly 2 elements appear only once and all the other 
# elements appear exactly twice. 
def singleNumber(nums: List[int]) -> int:
    return reduce(xor, nums) # XOR everything in array 

# Variation 2: Find the TWO elements that appear only ONCE. The rest of the array contains 
# paired numbers. Return the answer in any order. Example Input: nums = [1,2,1,3,2,5] --> [3,5]
def twoSingleNumbers(nums: List[int]) -> List[int]:
    # 1) Summary: XOR everything (otherXORs)
    # 2) Find the rightmost bit where the two remaining numbers differ
    # 3) Go through array again to find one of the unique numbers matching that bit
    # 4) XOR that number with otherXORs to find the second number
    
    # otherXORs is the XORing of everything in the array, resulting in num1^num2,
    # since every other paired number canceled each other out becoming 0000.
    otherXORs = reduce(xor, nums)

    # num1 and num2 are different, so they'll always have at least 1 bit difference
    # "Which bit is the rightmost bit that isn't shared among the 2?"
    nonzero_bit = (otherXORs & (otherXORs - 1)) ^ otherXORs 

    # Try to find number with that bit difference by traversing array again
    # Ex: 7 (0111) differs from 10 (1010) in the rightmost bit 0001
    # Another Ex: 2 (0010) differs from 9 (1001) in 0001
    # 0010^1001 = 1011
    # 1011 -> get rightmost bit = 0001
    # 0010 & 0001 (false), 1001 & 0001 = 0001 (true)
    
    # Filter the original array, "who of the unique two has this different bit?"
    # ex: 0001 0001 0010 1010 (1 1 2 8 8 10)
    # otherXORs = 0010 XOR 1010 = 1000, nonzero_bit = 1000
    # filter -> 0001 AND 1000 = 0000 (false), 0010 AND 1000 (false)
    # 1000 AND 1000 = 1000 (true, but gets canceled out with another 1000 so 0000)
    # 1010 AND 1000 (1000) (true) --> 0000 XOR 1010 = 1010 = num1
    num1 = reduce(xor, filter(lambda n: n & nonzero_bit, nums))

    # thus, num1 = 1010. 1010^1000 = 0010 = 2 = num2. Final answer = (10, 2)
    return (num1, num1^otherXORs)

# Variation 3: Given an integer array nums where every element appears THREE times 
# except for ONE, which appears exactly ONCE. Find the single element and return it.
def singleNumberInThreesArray(nums: List[int]) -> int:
    # To handle 3x occurrence, we can't use arrays, so use counter variables in bit form
    # Use finite state machine/bool logic to picture this.
    # 'incoming'  'second'  'unique'    'second'  'unique'
    #  0             0         0    |      0       0
    #  0             0         1    |      0       1
    #  0             1         0    |      1       0
    #  1             0         0    |      0       1
    #  1             0         1    |      1       0
    #  1             1         0    |      0       0  <- just clear it, we don't track thirds

    unique = 0 # unique = (unique ^ nums[i]) & ~second
    second = 0 # second = (second ^ nums[i]) & ~unique
    
    for number in nums:
        unique ^= (number & ~second) # can handle tracking all different consecutive uniques
        second ^= (number & ~unique) # shove the former unique here, if second becomes third, 0

    return unique

# Sanity check for the above functions
def XOR_test() -> None:
    print(bin(reduce(xor, [7, 1, 1, 5, 5, 10]))) # otherXORs = 1101

    # Property: num1 ^ num2 = otherXORs
    # Another observation: num1 ^ otherXORs = num2 (7 ^ 13 = 10)
    print("test: ", bin(7 ^ 10))
    print("test: ", bin(7 ^ 13)) # 0111 ^ 1010 = 1101 --> 0001
    print("test: ", bool(7 & 1)) # 0111 & 0001 = 0001
    print("test: ", bool(8 & 8)) # 0111 & 0001 = 0001
    print("test: ", bool(8 & ~8)) # 0111 & 0001 = 0001
    # 7 differs from 10 in that it has the rightmost bit 1

    # Python's Tilde ~n operator is the bitwise negation operator: 
    # it takes the number n as binary number and “flips” all bits 0 to 1 