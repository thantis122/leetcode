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
    def buildTree(self, preorder, inorder):
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
