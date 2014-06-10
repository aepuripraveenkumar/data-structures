

class Node(object):
    def __init__(self, node_name=None, node_next=None):
        self.node_name = node_name
        self.node_next = node_next


class Stack(object):
    def __init__(self):
        self.head = None

    def pop(self):
        try:
            self.head.node_next
        except AttributeError:
            raise
        else:
            temp = self.head.node_name
            self.head = self.head.node_next
        return temp

    def push(self, node_name):
        # the new head should point to the old head
        if not self.head:
            self.head = Node(node_name)
        else:
            self.head = Node(node_name, self.head)
