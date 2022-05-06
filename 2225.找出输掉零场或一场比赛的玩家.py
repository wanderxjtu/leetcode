#
# @lc app=leetcode.cn id=2225 lang=python3
#
# [2225] 找出输掉零场或一场比赛的玩家
#
from typing import List

# @lc code=start
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        losers = dict()
        for winner, loser in matches:
            winners.add(winner)
            losers[loser] = losers.get(loser, 0) + 1
        allwin = sorted(winners - set(losers.keys()))
        loseone = sorted(k for k, v in losers.items() if v == 1)
        return [allwin, loseone]


# @lc code=end
if __name__ == "__main__":
    inp = [
        [1, 3],
        [2, 3],
        [3, 6],
        [5, 6],
        [5, 7],
        [4, 5],
        [4, 8],
        [4, 9],
        [10, 4],
        [10, 9],
    ]
    print(Solution().findWinners(inp))
