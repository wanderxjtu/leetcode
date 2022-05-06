#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        import itertools
        n2l = dict(zip("0123456789", ("", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz")))
        return list(map("".join, itertools.product(*map(lambda n: n2l[n], digits))))
# @lc code=end


