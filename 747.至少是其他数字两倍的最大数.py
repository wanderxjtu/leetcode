#
# @lc app=leetcode.cn id=747 lang=python3
#
# [747] 至少是其他数字两倍的最大数
#
from typing import List

# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        maxi = 0
        m = -1
        s = -1
        for i, n in enumerate(nums):
            if n > m:
                maxi = i
                m, s = n, m
            elif n > s:
                s = n
        return maxi if m / 2 >= s else -1


# @lc code=end
if __name__ == "__main__":
    r = Solution().dominantIndex([1, 2, 3, 4])
    r = Solution().dominantIndex([3, 2, 7, 1, 0])
    r = Solution().dominantIndex([3, 6, 1, 0])
    r = Solution().dominantIndex([1, 0])
    r = Solution().dominantIndex([0, 1])
    print(r)
