#
# @lc app=leetcode.cn id=1073 lang=python3
#
# [1073] 负二进制数相加
#
from typing import List
from functools import reduce, lru_cache
from operator import add

# @lc code=start
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        p1, n1 = tuple(arr1[::-2]), tuple(arr1[-2::-2])
        p2, n2 = tuple(arr2[::-2]), tuple(arr2[-2::-2])

        @lru_cache(None)
        def a2i(arr):
            if not arr:
                return 0
            return reduce(add, (b << i * 2 for i, b in enumerate(arr)))

        def i2a(i):
            num = i
            r = []
            while True:
                r.append(num & 1)
                n = num & 2
                num = num >> 2
                if n == 2:
                    num += 1
                    n = 1
                r.append(n)
                if not num:
                    break
            if r[-1] == 0:
                r.pop()
            return r

        reti = a2i(p1) + a2i(p2) - ((a2i(n1) + a2i(n2)) << 1)
        print(a2i(p1), a2i(p2), a2i(n1), a2i(n2))
        print(reti)
        return i2a(reti)[::-1]


# @lc code=end

if __name__ == "__main__":
    print(Solution().addNegabinary([1, 1, 1, 1, 1], [1, 0, 1]))
    print(Solution().addNegabinary([0], [0]))
    print(Solution().addNegabinary([0], [1]))
    print(Solution().addNegabinary([1], [1]))
