from typing import List
#--------------------------------------------------------------------------------------------------
class TwoPointer:
# 2) Two Pointer Technique: Similar to sliding window, "search for a pair in SORTED" array,
#     Find a "cycle" within a Linked List (fast-slow pointer).
#     Also O(N) since array is traversed only once.

    # Ex: 2 arrays nums1 and nums2 are already sorted in increasing order. nums1 has size m + n
    #    Where n are the extra 0s in nums1 that are placeholders for the extra numbers added from
    #    nums2. nums2.length == n. Assume negative and positive integers in both arrays.
    #    Merge them into a single array sorted in increasing order.
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        leftEnd, rightEnd = m - 1, n - 1 # represents position of real numbers
        # L = current position starting from the back (including empty spots)
        for L in reversed(range(m+n)):
            if (rightEnd < 0): # right array has been used up
                break
            if (leftEnd < 0): # add the rest of right array into left
                nums1[:L + 1] = nums2[:rightEnd + 1]
                break
            if (nums2[rightEnd] >= nums1[leftEnd]): # put the bigger of the two 
                nums1[L] = nums2[rightEnd]
                rightEnd -= 1
            else:
                nums1[L] = nums1[leftEnd]
                leftEnd -= 1

#--------------------------------------------------------------------------------------------------
    # Returns the length of the longest substring w/out repeating characters.
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        start = 0
        end = 0
        string_sofar = ""
        for c in s:
            if c in string_sofar:
                longest = max(longest, len(string_sofar))
                start = string_sofar.index(c) + 1 # get rid of offending repeat character
                string_sofar += c # add new repeat character at the end
                string_sofar = string_sofar[start:]
            else: # if no repeats yet, keep adding
                string_sofar += c 
                end += 1
        return max(longest, len(string_sofar))

#--------------------------------------------------------------------------------------------------
    # Returns True if there is a cycle in a given LinkedList.
    def hasCycle(ll): # Assume only singley linked and all nodes point to null/node
        if not ll or not ll.next: # the list ends somewhere / isn't just 1 node
            return False
        fastPointer = ll.next # fast starts off second node, advances 2x
        slowPointer = ll
        while fastPointer and fastPointer.next:
            # if the two ever meet
            if fastPointer == slowPointer or fastPointer.next == slowPointer: 
                return True
            fastPointer = fastPointer.next.next
            slowPointer = slowPointer.next
        return False