#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# --------------------------------------
# DATE: 2018/2/28


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    :type root: TreeNode
    :rtype: bool
    :type sum: int
    """

    def hasPathSum(self, root, sum):
        if root == None:
            return False
        if root.left == None and root.right == None:
            return root.val == sum
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)


if __name__ == "__main__":
    root = TreeNode(5)
    root.left, root.right = TreeNode(4), TreeNode(8)
    root.left.left, root.right.left, root.right.right = TreeNode(11), TreeNode(13), TreeNode(4)
    root.left.left.left, root.left.left.right, root.right.right.right = TreeNode(7), TreeNode(2), TreeNode(1)
    print(Solution().hasPathSum(root, 22))
