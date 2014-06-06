


class Node(object):
    def __init__(self, node_name=None, node_next=None):
        self.node_name = node_name
        self.node_next = node_next

class Stack(object):
    def __init__(self):
        self.head = None

    def pop(self):
        old_head = self.head
        try:
            old_head.node_next
        except AttributeError:
            return "The stack is empty."
        else:
            new_head = self.head.node_next
            self.head = new_head
        return old_head.node_name

    def push(self, node_name):
        # the new head should point to the old head
        if not self.head:
            node = Node(node_name)
            self.head = node
        else:
            old_head = self.head
            node = Node(node_name, old_head)
            self.head = node