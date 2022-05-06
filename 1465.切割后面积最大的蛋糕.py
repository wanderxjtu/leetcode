#
# @lc app=leetcode.cn id=1465 lang=python3
#
# [1465] 切割后面积最大的蛋糕
#
from typing import List
from itertools import pairwise

# @lc code=start
class Solution:
    def maxArea(
        self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]
    ) -> int:
        horizontalCuts.insert(0, 0)
        horizontalCuts.append(h)
        horizontalCuts.sort()
        verticalCuts.insert(0, 0)
        verticalCuts.append(w)
        verticalCuts.sort()
        mh = max(j - i for i, j in pairwise(horizontalCuts))
        mv = max(j - i for i, j in pairwise(verticalCuts))
        return mh * mv % (10**9 + 7)


# @lc code=end
if __name__ == "__main__":
    h = 5
    w = 4
    horizontalCuts = [1, 2, 4]
    verticalCuts = [1, 3]
    print(Solution().maxArea(h, w, horizontalCuts, verticalCuts))
    h = 5
    w = 4
    horizontalCuts = [3, 1]
    verticalCuts = [1]
    print(Solution().maxArea(h, w, horizontalCuts, verticalCuts))
