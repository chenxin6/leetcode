from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    db = {}

    def rob(self, root: Optional[TreeNode]) -> int:
        return self.my_method(root, True)

    def my_method(self, root: Optional[TreeNode], can_rob: bool) -> int:
        if root is None:
            return 0
        key = str(root) + "-" + str(can_rob)
        if self.db.get(key) is not None:
            return self.db[key]
        res = 0
        if can_rob:
            res = root.val + self.my_method(root.left, False) + self.my_method(root.right, False)
        temp_res = self.my_method(root.left, True) + self.my_method(root.right, True)
        res = max(res, temp_res)
        self.db[key] = res
        return res


s = Solution()
node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
print(s.rob(node))
