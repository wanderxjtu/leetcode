#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
from typing import List

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        revdict = {}
        for i, ni in enumerate(nums):
            try:
                return [revdict[target - ni], i]
            except KeyError:
                revdict[ni] = i


# @lc code=end
if __name__ == "__main__":
    ret = Solution().twoSum([100, 3, -1, 2, 4], 6)
    print(ret)
