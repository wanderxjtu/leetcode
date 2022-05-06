#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
from tkinter import N
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        print(self.val)
        if self.next:
            self.next.print()


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        if not l1:
            return l2
        if not l2:
            if l1.val < 10:
                return l1
            l2 = ListNode()
        ret = ListNode()
        k = l1.val + l2.val
        ret.val = k % 10
        if k >= 10:
            if l1.next is None:
                l1.next = ListNode(1)
            else:
                l1.next.val += 1
        ret.next = self.addTwoNumbers(l1.next, l2.next)
        return ret


# @lc code=end
if __name__ == "__main__":
    l2 = ListNode(9, ListNode(9))
    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    Solution().addTwoNumbers(l1, l2).print()
