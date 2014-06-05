

class Node(object):
    def __init__(self, name=None, next=None):
        self.name = name
        self.next = next

    def __str__(self):
        return str(self.name)


class Linked_List(object):
    def __init__(self):
        self.size = 0
        self.head = None

    def __str__(self):
        pass

    # insert node at head
    def insert(self, name):
        # the new head should point to the old head
        if self.head is None:
            node = Node(name)
            self.head = node
        else:
            old_head = self.head
            node = Node(name, old_head)
            self.head = node
        self.size += 1

    # pop the first value off the head of the list and return it
    def pop(self):
        old_head = self.head
        new_head = self.head.next
        self.head = new_head
        self.size -= 1
        return old_head

    def size(self):
        return self.size

    # return node containing val in list, if present, else None
    def search(self, name):
        temp = self.head
        while temp.next is not None:
            if temp.name == name:
                return temp
            else:
                temp = temp.next
        return None
        pass

    # rmove given node from list, node must be in list
    def remove(node):
        pass
