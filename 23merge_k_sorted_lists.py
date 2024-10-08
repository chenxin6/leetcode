from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = self.myMethod(lists)
        n = len(arr)
        root = ListNode(0)
        tempNode = root
        while n > 0 and type(arr[0]) is ListNode:
            tempNode.next = ListNode(arr[0].val)
            tempNode = tempNode.next
            arr[0] = arr[0].next
            self.adjust(arr, 0, n)
        return root.next

    def myMethod(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for node in lists:
            arr.append(node)
        n = len(arr)
        for i in range(n // 2, n):
            self.adjust(arr, n - i - 1, n)
        return arr

    def adjust(self, arr, i, n):
        fatherValue = None
        if arr[i] is not None:
            fatherValue = arr[i]
        while self.getLeftChild(i) < n:
            child = self.getLeftChild(i)
            if child + 1 < n and (arr[child] is None or (arr[child + 1] is not None and arr[child].val > arr[child + 1].val)):
                child += 1
            if fatherValue is not None and arr[child] is not None and fatherValue.val <= arr[child].val:
                break
            elif arr[child] is None:
                break
            else:
                self.swap(arr, i, child)
                i = child
        arr[i] = fatherValue

    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def getLeftChild(self, i):
        return 2 * i + 1


s = Solution()
a = ListNode(1)
a.next = ListNode(4)
a.next.next = ListNode(5)
b = ListNode(1)
b.next = ListNode(3)
b.next.next = ListNode(4)
c = ListNode(2)
c.next = ListNode(6)
res = s.mergeKLists([a, b, c])
while res is not None:
    print(res.val)
    res = res.next
