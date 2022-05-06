#
# @lc app=leetcode.cn id=446 lang=python3
#
# [446] 等差数列划分 II - 子序列
#
from email.policy import default
from typing import List
from itertools import product, combinations
from collections import defaultdict
from functools import partial

# @lc code=start
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        total = 0
        trans = [defaultdict(int) for _ in nums]
        # seq[i][d] means the member of sub-seqs starting with element i of differece d
        for i, j in combinations(range(len(nums)), 2):
            # i < j
            d = nums[i] - nums[j]
            total += trans[i][d]
            trans[j][d] += trans[i][d] + 1
        return total


# @lc code=end
if __name__ == "__main__":
    a = [2, 4, 6, 8, 10]
    print(Solution().numberOfArithmeticSlices(a))
    a = [7] * 5
    print(Solution().numberOfArithmeticSlices(a))
