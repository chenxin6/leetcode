class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head
        pre_head = ListNode(0)
        pre_head.next = head
        pre_current_root_node = pre_head
        current_root_value = None
        current_node = head
        after_current_node = head.next
        while after_current_node is not None:
            if current_root_value is None:
                if current_node.val == after_current_node.val:
                    current_root_value = current_node.val
                    pre_current_root_node.next = after_current_node
                else:
                    current_root_value = None
                    pre_current_root_node = current_node
            else:
                if current_node.val == after_current_node.val:
                    current_root_value = current_node.val
                else:
                    current_root_value = None
                pre_current_root_node.next = after_current_node
            current_node = after_current_node
            after_current_node = after_current_node.next
        if after_current_node is None and current_root_value is not None:
            pre_current_root_node.next = None
        return pre_head.next
    

A = Solution()
root = ListNode(1)
root.next = ListNode(1)
root.next.next = ListNode(1)
root.next.next.next = ListNode(2)
root.next.next.next.next = ListNode(4)
root.next.next.next.next.next = ListNode(5)
root.next.next.next.next.next.next = ListNode(5)
temp_node = A.deleteDuplicates(root)
while temp_node is not None:
    print(temp_node.val)
    temp_node = temp_node.next