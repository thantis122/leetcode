#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# --------------------------------------
# DATE: 2018/2/28
# input inorder[9,3,15,20,7] postorder[9,15,7,20,3]
# output [3,9,20,null,null,15,7]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            rootInd = inorder.index(postorder.pop())
            rroot = TreeNode(inorder[rootInd])
            rroot.right = self.buildTree(inorder[rootInd + 1:], postorder)
            rroot.left = self.buildTree(inorder[:rootInd], postorder)
            return rroot
