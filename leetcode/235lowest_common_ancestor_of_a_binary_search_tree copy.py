# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def get_link(self, root: "TreeNode", target: "TreeNode") -> list["TreeNode"]:
        res = []
        temp_list: list[TreeNode | str] = [root]
        while temp_list:
            temp_node = temp_list.pop()
            if isinstance(temp_node, TreeNode):
                res.append(temp_node)
                if temp_node.val == target.val:
                    break
                temp_list.append("res pop")
                if temp_node.left is not None:
                    temp_list.append(temp_node.left)
                if temp_node.right is not None:
                    temp_list.append(temp_node.right)
            else:
                res.pop()
        return res

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        p_link = self.get_link(root, p)
        q_link = self.get_link(root, q)

        res = None
        for i in range(min(len(p_link), len(q_link)) - 1):
            if p_link[i + 1].val != q_link[i + 1].val:
                res = p_link[i]
                break
        if res is None:
            res = p if len(p_link) < len(q_link) else q

        return res


test_root = TreeNode(6)
test_p = TreeNode(2)
test_q = TreeNode(8)
test_root.left = test_p  # type: ignore
test_root.right = test_q  # type: ignore
print(Solution().lowestCommonAncestor(test_root, test_p, test_q).val)
