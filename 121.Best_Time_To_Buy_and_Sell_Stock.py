import logging

class Solution:
    def maxProfit(self, prices) -> int:
        profit=0   # initial profit
        buyp=prices[0]
        for p in prices:
            if p < buyp:
                buyp = p
                continue
            if p - buyp > profit:
                profit = p - buyp
        return profit





import unittest
class TestMaxProfit(unittest.TestCase):
    def testMaxProfit(self):
        self.assertEqual(Solution().maxProfit([7,1,5,3,6,4]), 5)
        self.assertEqual(Solution().maxProfit([7,6,4,3,1]), 0)

unittest.main()
        
