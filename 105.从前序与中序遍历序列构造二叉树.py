#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#
from typing import List

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def traverse(self, nid=1):
        yield nid, self.val
        if self.left:
            yield from self.left.traverse(nid * 2)
        if self.right:
            yield from self.right.traverse(nid * 2 + 1)


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return
        rval = preorder[0]
        root = TreeNode(rval)
        if len(preorder) == 1:
            return root
        inc = inorder.index(rval)
        root.left = self.buildTree(preorder[1 : inc + 1], inorder[:inc])
        root.right = self.buildTree(preorder[inc + 1 :], inorder[inc + 1 :])
        return root


# @lc code=end
if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    t = Solution().buildTree(preorder, inorder)
    print(list(t.traverse()))
    preorder = [1, 2]
    inorder = [2, 1]
    t = Solution().buildTree(preorder, inorder)
    print(list(t.traverse()))
