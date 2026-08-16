from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        item_list = []
        item_list.append(root)
        while len(item_list) > 0:
            item = item_list.pop(0)
            if item is None:
                continue
            if isinstance(item, TreeNode):
                item_list.insert(0, item.right)
                item_list.insert(0, item.val)
                item_list.insert(0, item.left)
            else:
                res.append(item)
        return res

    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            return [root.val]
        return (
            self.inorderTraversal2(root.left)
            + [root.val]
            + self.inorderTraversal2(root.right)
        )
