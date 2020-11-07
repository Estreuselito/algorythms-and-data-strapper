class Entry:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Double_linked:

    def __init__(self):
        self.head = None

    def add(self, data):
        entry = Entry(data)
        entry.next = self.head
        if self.head is not None:
            self.head.prev = entry
        self.head = entry

    def insert(self, prev_node, data):
        if prev_node is None:
            return
        entry = Entry(data)
        entry.next = prev_node.next
        entry.prev = prev_node
        prev_node.next = entry
        if entry.next is not None:
            entry.next.prev = entry

    def print_list(self, entry):
        while (entry is not None):
            print(entry.data)
            last = entry
            entry = entry.next