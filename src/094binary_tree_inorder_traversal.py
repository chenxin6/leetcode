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
            if type(item) is TreeNode:
                item_list.insert(0, item.right)
                item_list.insert(0, item.val)
                item_list.insert(0, item.left)
            else:
                res.append(item)
        return res
