# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None or (root.left is None and root.right is None):
            return root
        # reversed_left = self.invertTree(root.left)
        # reversed_right = self.invertTree(root.right)
        # root.left = reversed_right
        # root.right = reversed_left
        # return root
        l = []
        l.append(root)
        while len(l) > 0:
            temp_node = l.pop(0)
            temp_node_left = temp_node.left
            temp_node_right = temp_node.right
            if temp_node_left is not None:
                l.append(temp_node_left)
            if temp_node_right is not None:
                l.append(temp_node_right)
            temp_node.left = temp_node_right
            temp_node.right = temp_node_left
        return root