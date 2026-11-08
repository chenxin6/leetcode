class LinkNode:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev: LinkNode | None = None
        self.next: LinkNode | None = None


class LRUCache:

    def __init__(self, capacity: int):
        self.my_dict: dict[int, LinkNode] = {}
        self.capacity = capacity
        self.head = LinkNode(-1, -1)
        self.tail = LinkNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.my_dict:
            return -1
        node = self.my_dict[key]
        self.__pop_node(node)
        self.__insert_node(self.head, node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.my_dict:
            node = self.my_dict[key]
            node.value = value
            self.__pop_node(node)
        else:
            node = LinkNode(key, value)
            self.my_dict[key] = node
        self.__insert_node(self.head, node)
        if len(self.my_dict) > self.capacity:
            temp_node = self.tail.prev
            if temp_node is not None:
                self.my_dict.pop(temp_node.key)
                self.__pop_node(temp_node)

    def __insert_node(self, target: LinkNode, node: LinkNode) -> None:
        temp_next = target.next
        if temp_next is not None:
            target.next = node
            node.prev = target
            node.next = temp_next
            temp_next.prev = node

    def __pop_node(self, node: LinkNode) -> None:
        if node.prev is not None and node.next is not None:
            node.prev.next = node.next
            node.next.prev = node.prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
