"""Implements a double-linked list data structure"""


class Node(object):
    def __init__(self, node_name, node_next=None, node_prev=None):
        self.node_name = node_name
        self.node_next = node_next
        self.node_prev = node_prev


class Double_list(object):
    def __init__(self):
        self.list_ptr = None

    def pop(self):
        return_value = self.list_ptr.node_name
        self.list_ptr = self.list_ptr.node_next
        self.list_ptr.node_prev = None
        return return_value

    def shift(self):
        temp = self.list_ptr
        while temp.node_next:
            temp = temp.node_next
        return_value = temp.node_name
        temp = temp.node_prev
        temp.node_next = None
        return return_value

    def insert(self, node_name):
        # the new head should point to the old head
        if not self.list_ptr:
            self.list_ptr = Node(node_name)
        else:
            temp = self.list_ptr
            self.list_ptr = Node(node_name, temp)
            temp.node_prev = self.list_ptr

    def append(self, node_name):
        temp = self.list_ptr
        while temp.node_next:
            temp = temp.node_next
        temp.node_next = Node(node_name, None, temp)

    def remove(self, value):
        temp = self.list_ptr
        try:
            while temp.node_name != value:
                temp = temp.node_next
        except AttributeError:
            raise AttributeError
        else:
            temp.node_next.node_prev = temp.node_prev
            temp.node_prev.node_next = temp.node_next
