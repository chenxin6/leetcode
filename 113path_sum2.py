# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        if root is None:
            return res
        if root.left is None and root.right is None:
            if targetSum == root.val:
                res.append([root.val])
            return res
        left_res = []
        right_res = []
        if root.left is not None:
            left_res = self.pathSum(root.left, targetSum - root.val)
        if root.right is not None:
            right_res = self.pathSum(root.right, targetSum - root.val)
        temp_res = [root.val]
        for temp in left_res:
            res.append(temp_res + temp)
        for temp in right_res:
            res.append(temp_res + temp)
        return res
