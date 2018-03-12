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


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        path = []
        if root is None:
            return path
        stack = []
        stack.append(root)
        while stack:
            root = stack.pop()
            path.append(root.val)
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)
        return path
