from typing import Dict, List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        res = False
        if root is None:
            return res
        if root.left is None and root.right is None:
            if targetSum == root.val:
                res = True
            return res
        left_res = False
        right_res = False
        if root.left is not None:
            left_res = self.hasPathSum(root.left, targetSum - root.val)
        if root.right is not None:
            right_res = self.hasPathSum(root.right, targetSum - root.val)
        return left_res or right_res
