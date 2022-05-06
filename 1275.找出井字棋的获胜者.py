#
# @lc app=leetcode.cn id=1275 lang=python3
#
# [1275] 找出井字棋的获胜者
#
from re import M
from typing import List

# @lc code=start
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        if len(moves) < 5:
            return "Pending"
        ma = tuple(map(tuple, moves[::2]))
        mb = tuple(map(tuple, moves[1::2]))
        for w in [
            set(((0, 0), (1, 0), (2, 0))),
            set(((0, 1), (1, 1), (2, 1))),
            set(((0, 2), (1, 2), (2, 2))),
            set(((0, 0), (0, 1), (0, 2))),
            set(((1, 0), (1, 1), (1, 2))),
            set(((2, 0), (2, 1), (2, 2))),
            set(((0, 0), (1, 1), (2, 2))),
            set(((2, 0), (1, 1), (0, 2))),
        ]:
            if w - set(ma) == set():
                return "A"
            if w - set(mb) == set():
                return "B"
        if len(moves) == 9:
            return "Draw"
        return "Pending"


# @lc code=end
if __name__ == "__main__":
    moves = [[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]]
    print(Solution().tictactoe(moves))
    moves = [[0, 0], [1, 1]]
    print(Solution().tictactoe(moves))
    moves = [[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]]
    print(Solution().tictactoe(moves))
    moves = [[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]
    print(Solution().tictactoe(moves))
