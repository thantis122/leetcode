#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# --------------------------------------
# DATE: 2018/3/2


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, preorder):
        '''

        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        '''

        if preorder:
            rootPre = inorder.index(preorder[0])
            rroot = TreeNode(inorder[rootPre])
            rroot.right = self.buildTree(inorder[rootPre + 1:], preorder)
            rroot.left = self.buildTree(inorder[:rootPre], preorder)
            return rroot





# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.preorder = preorder
        self.inorder = inorder
        return self._buildTree(0, len(preorder), 0, len(inorder))

    def _buildTree(self, pre_start, pre_end, in_start, in_end):
        if pre_start >= pre_end:
            return None
        root = TreeNode(self.preorder[pre_start])
        offset = self.inorder[in_start:in_end + 1].index(root.val)
        root.left = self._buildTree(pre_start + 1, pre_start + offset + 1, in_start, in_start + offset)
        root.right = self._buildTree(pre_start + offset + 1, pre_end, in_start + offset + 1, in_end)
        return root


if __name__ == "__main__":
    None