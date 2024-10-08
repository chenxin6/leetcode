class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        # return self.countNodes(root.left) + self.countNodes(root.right) + 1
        l = []
        l.append(root)
        res = 0
        while len(l) > 0:
            temp = l.pop(0)
            if temp.left is not None:
                l.append(temp.left)
            if temp.right is not None:
                l.append(temp.right)
            res += 1
        return res

    
