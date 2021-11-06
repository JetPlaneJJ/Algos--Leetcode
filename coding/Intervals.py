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
#--------------------------------------------------------------------------------------------------
    # Given an array of intervals where intervals[i] = [starti, endi], 
    # merge all overlapping intervals, and return an array of the non-overlapping intervals that 
    # cover all the intervals in the input. Assume intervals.length >= 1, start <= end.
    # Example Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort all intervals
        intervals.sort(key= lambda interval: interval[0])
        merged_intervals : List[List[int]] = []
        
        for start, end in intervals:
            if merged_intervals == []:
                merged_intervals.append([start, end])
            else:
                if (start <= merged_intervals[-1][1]): # overlap
                    merged_intervals[-1][1] = max(end, merged_intervals[-1][1])
                else:
                    merged_intervals.append([start, end])

        return merged_intervals