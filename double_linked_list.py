import time


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Double_linked:

    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node

    def insert(self, prev_node, data):
        if prev_node is None:
            return
        node = Node(data)
        node.next = prev_node.next
        node.prev = prev_node
        prev_node.next = node
        if node.next is not None:
            node.next.prev = node

    def push(self, data):
        node = Node(data)
        node.next = self.head
        node.prev = None
        if self.head is not None:
            self.head.prev = node

        self.head = node

    def print_list(self, node):
        while (node is not None):
            print(node.data)
            last = node
            node = node.next


def time_complexity_linked_list(n, insert_node_data):
    """
    ll : object
        linked list

    n : int
        n stands for the length of the list
    """
    ll = Double_linked()
    for i in range(0, n):
        # as soon as you initialize the object self is also initialized within that object. This means it is in the object; you don't need to re-input it.
        ll.add(data=i)
    start = time.time()
    ll.insert(ll.head, insert_node_data)
    end = start - time.time()
    print(f"The insert to the linked list of length {n} took {end} seconds")
    return ll


numbers = [400, 800, 1600, 3200, 6400, 12800, 25600, 51200]

for n in numbers:
    time_complexity_linked_list(n, 134)
