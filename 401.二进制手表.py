#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#
from typing import List
from itertools import combinations

# @lc code=start
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ret = []
        for c in combinations((1, 2, 4, 8, 16, 32, 64, 128, 256, 512), turnedOn):
            total = sum(c)
            H = 0b1111 & total
            if H > 11:
                continue
            M = total >> 4
            if M > 59:
                continue
            ret.append("%d:%02d" % (H, M))
        return ret


# @lc code=end

if __name__ == "__main__":
    for i in range(11):
        print(Solution().readBinaryWatch(i))
