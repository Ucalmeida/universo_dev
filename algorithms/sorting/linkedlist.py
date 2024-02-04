class Node:
    def __init__(self, value):
        self.next = None
        self.value = value


class LinkedList:
    def __init__(self):
        self.__head = Node(None)

    def insert_node_to_tail(self, node):
        self.tail().next = node

    def insert_node_to_head(self, node):
        if self.__head.next:
            head_element = self.__head
            node.next, head_element = head_element.next, node
        self.__head.next = node

    def is_empty(self):
        return self.__head.next is None

    def head(self):
        return self.__head.next

    def tail(self):
        pointer = self.__head
        while pointer.next:
            pointer = pointer.next
        return pointer

