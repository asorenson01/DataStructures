from node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_node(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
            return
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def add_to_beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        print("hello world")

    def contains_node(self):
        x = self.head
        while x.next is not None:
            print(f'{x.data}')
            x = x.next
