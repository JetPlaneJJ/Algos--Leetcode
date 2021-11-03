from typing import List
#--------------------------------------------------------------------------------------------------
# Ideal solutions: Time = O(NlogN), Space = O(1) extra space
# General steps:
# 1) Sort all intervals in increasing order of START time.
# 2) For each interval starting from first...
#       a) WHILE the current interval is NOT first and overlaps with the previous one, 
#          merge it with the previous interval
#       b) ELSE add current interval to output list of intervals.
class TwoPointer:
#--------------------------------------------------------------------------------------------------
    # Given an array of time INTERVALS in any order, "MERGE all overlapping intervals into one" 
    # and print the result, which should have only mutually exclusive intervals.
    # Let the intervals be represented as pairs of integers for simplicity.
    def mergeIntervals(times: List[int]) -> None:
        
        ...
    ...