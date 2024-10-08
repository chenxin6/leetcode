class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l = self.get_list(root)
        return l[k - 1]
    def get_list(self, root: Optional[TreeNode]):
        res = []
        # if root.left is not None:
        #     res += self.get_list(root.left)
        # res.append(root.val)
        # if root.right is not None:
        #     res += self.get_list(root.right)
        l = []
        l.append(root)
        while len(l) > 0:
            temp_value = l.pop(0)
            if temp_value is None:
                continue
            if type(temp_value) is TreeNode:
                l.insert(0, temp_value.right)
                l.insert(0, temp_value.val)
                l.insert(0, temp_value.left)
            else:
                res.append(temp_value)
        return res