#
# @lc app=leetcode.cn id=934 lang=python3
#
# [934] 最短的桥
#
from typing import List
from itertools import product

# @lc code=start
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        dim = len(grid)
        groupA = set()

        def check(x, y):
            if x < 0 or y < 0 or x >= dim or y >= dim:
                return
            if not grid[x][y]:
                return
            if (x, y) in groupA:
                return
            groupA.add((x, y))
            findNext(x, y)

        def findNext(x, y):
            # print(x, y)
            check(x - 1, y)
            check(x + 1, y)
            check(x, y - 1)
            check(x, y + 1)

        def distance(x, y):
            return min(abs(x - i) + abs(y - j) - 1 for i, j in group)

        mindis = 2 * dim
        for i, j in product(range(dim), repeat=2):
            if grid[i][j]:
                if groupA:
                    if (i, j) not in groupA:
                        mindis = min(distance(i, j), mindis)
                        if mindis == 1:
                            return 1
                else:
                    groupA.add((i, j))
                    findNext(i, j)
                    print(groupA)
        return mindis


# @lc code=end
if __name__ == "__main__":
    print(Solution().shortestBridge([[0, 1], [1, 0]]))
    print("-" * 70)
    g = [
        [0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0],
        [1, 0, 0, 0, 0],
        [1, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
    ]
    g = [
        [1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1],
    ]
    try:
        print(Solution().shortestBridge(g))
    except RecursionError:
        pass
