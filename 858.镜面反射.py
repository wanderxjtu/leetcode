#
# @lc app=leetcode.cn id=858 lang=python3
#
# [858] 镜面反射
#

# @lc code=start
import math


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        if q == p:
            return 1
        lcm = math.lcm(p, q)
        if int(lcm / q) % 2 == 0:
            return 2
        return int(lcm / p) % 2


# @lc code=end
if __name__ == "__main__":
    p = 2
    q = 1
    print(Solution().mirrorReflection(p, q))
    p = 5
    q = 2
    print(Solution().mirrorReflection(p, q))
