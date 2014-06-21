"""Implements a queue data structure"""



class Node(object):
    def __init__(self, node_name, node_next=None, node_prev=None):
        self.node_name = node_name
        self.node_next = node_next
        self.node_prev = node_prev


class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def dequeue(self):
        try:
            self.head.node_name
        except AttributeError:
            raise
        else:
            temp = self.head.node_name
            if self.size > 1:
                self.head = self.head.node_prev
                self.head.node_next = None
            else:
                self.head = None
            self.size -= 1
        return temp

    def enqueue(self, node_name):
        # the new head should point to the old head
        if not self.head:
            self.head = Node(node_name)
            self.tail = self.head
        else:
            temp = self.tail
            self.tail = Node(node_name, temp)
            temp.node_prev = self.tail
        self.size += 1
