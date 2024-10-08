from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        if root is None:
            return res
        if root.left is None and root.right is None:
            res.append(str(root.val))

        temp_res = self.binaryTreePaths(root.left)
        temp_res += self.binaryTreePaths(root.right)
        for temp_str in temp_res:
            res.append(str(root.val) + "->" + temp_str)
        
        return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
s = Solution()
res = s.binaryTreePaths(root)
for temp_str in res:
    print(temp_str)
