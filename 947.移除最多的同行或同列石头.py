#
# @lc app=leetcode.cn id=947 lang=python3
#
# [947] 移除最多的同行或同列石头
#
from typing import List
from collections import defaultdict

# @lc code=start
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        if len(stones) == 1:
            return 0
        xs, ys = defaultdict(set), defaultdict(set)
        for x, y in stones:
            xs[x].add((x, y))
            ys[y].add((x, y))

        allx = set(xs.keys())

        def expandx(x):
            for _, y in xs[x]:
                if (x, y) not in ans:
                    ans.add((x, y))
                    allx.discard(x)
                    expandy(y)
            return

        def expandy(y):
            for x, _ in ys[y]:
                if (x, y) not in ans:
                    ans.add((x, y))
                    allx.discard(x)
                    expandx(x)
            return

        grpCount = 0
        groups = []
        while allx:
            ans = set()
            expandx(allx.pop())
            groups.append(ans)
            grpCount += 1
        print(groups)

        return len(stones) - grpCount


if __name__ == "__main__":
    stones = [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]
    print(Solution().removeStones(stones))
    stones = [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]]
    print(Solution().removeStones(stones))
    stones = [[0, 0]]
    print(Solution().removeStones(stones))
    stones = [[0, 1], [1, 0], [1, 1]]
    print(Solution().removeStones(stones))
    stones = [[0, 1], [1, 1]]
    print(Solution().removeStones(stones))
