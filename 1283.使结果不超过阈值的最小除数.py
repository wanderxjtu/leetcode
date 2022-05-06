#
# @lc app=leetcode.cn id=1283 lang=python3
#
# [1283] 使结果不超过阈值的最小除数
#
from typing import List
import math

# @lc code=start
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        total = sum(nums)
        f = math.ceil(total / threshold)
        t = max(nums)
        return self._search(f, t, nums, threshold)

    def _search(self, fr, to, nums, threshold):
        if to == fr:
            return to
        n = math.floor((fr + to) / 2)
        if self._check(nums, n, threshold):
            return self._search(fr, n, nums, threshold)
        else:
            return self._search(n + 1, to, nums, threshold)

    def _check(self, nums, n, threshold):
        return sum(math.ceil(a / n) for a in nums) <= threshold


# @lc code=end
if __name__ == "__main__":
    r = Solution().smallestDivisor([1, 2, 5, 9], 6)
    r = Solution().smallestDivisor([1, 2, 3], 6)
    print(r)
    r = Solution().smallestDivisor([21212, 10101, 12121], 1000000)
    print(r)
