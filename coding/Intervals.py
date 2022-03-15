from typing import List
#--------------------------------------------------------------------------------------------------
# Ideal solutions: Time = O(NlogN), Space = O(1) extra space
# General steps:
# 1) Sort all intervals in increasing order of START time.
# 2) For each interval starting from first...
#       a) WHILE the current interval is NOT first and overlaps with the previous one, 
#          merge it with the previous interval
#       b) ELSE add current interval to output list of intervals.
class Intervals:

# --------------------------------------------------------------------------------------------------
    # Easy Merged intervals variation.
    # Given integers i,j,k, find the total sum from numbers i up to j, and back down to k inclusive.
    # Ex: getSequenceSum(0, 2, -1) = 0 + 1 + 2 + 1 + 0 + -1 = 3
    def getSequenceSum(self, i, j, k):
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

#--------------------------------------------------------------------------------------------------
    # Given an array of intervals where intervals[i] = [starti, endi], 
    # merge all overlapping intervals, and return an array of the non-overlapping intervals that 
    # cover all the intervals in the input. Assume intervals.length >= 1, start <= end.
    # Example Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1. sort all intervals
        intervals.sort(key= lambda interval: interval[0])
        merged_intervals : List[List[int]] = []
        
        for start, end in intervals:
            if merged_intervals == []:
                merged_intervals.append([start, end]) # 2. the very first interval already merged
            else:
                if (start <= merged_intervals[-1][1]): # 3. combine overlapped with last seen
                    merged_intervals[-1][1] = max(end, merged_intervals[-1][1])
                else:
                    merged_intervals.append([start, end])

        return merged_intervals