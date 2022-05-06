#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int],
                               nums2: List[int]) -> float:
        if not nums1:
            return self._findMedian(nums2)[0]
        if not nums2:
            return self._findMedian(nums1)[0]
        return self._findMedianSortedArrays(nums1, nums2)

    def _findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) == 1:
        if len(nums2) == 1:

        mid1, mi1 = self._findMedian(nums1)
        mid2, mi2 = self._findMedian(nums2)
        if mid1 == mid2:
            return mid1
        if mid1 > mid2:  # swap
            nums1, nums2 = nums2, nums1
            mid1, mid2 = mid2, mid1
            mi1, mi2 = mi2, mi1
        if mi1 == 0:
            return self._findMedian

        return self._findMedianSortedArrays(nums1, nums2)
        # now m2 > m1:

        l = sorted(nums1 + nums2)

    def _findCentral(self, nums):
        fl = len(nums)
        if fl % 2 == 0:
            md = int(fl / 2)
            return [nums[md - 1], nums[md]], md
        else:
            md = int((fl - 1) / 2)
            return nums[md-1, md+2], md


# @lc code=end
