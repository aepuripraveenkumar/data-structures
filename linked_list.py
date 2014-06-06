

class Node(object):
    def __init__(self, node_name=None, node_next=None):
        self.node_name = node_name
        self.node_next = node_next

    def __str__(self):
        return str(self.node_name)


class Linked_List(object):
    def __init__(self):
        self.size = 0
        self.head = None

    # insert node at head
    def insert(self, node_name):
        # the new head should point to the old head
        if self.head is None:
            node = Node(node_name)
            self.head = node
        else:
            old_head = self.head
            node = Node(node_name, old_head)
            self.head = node
        self.size += 1

    # pop the first value off the head of the list and return it
    def pop(self):
        old_head = self.head
        new_head = self.head.node_next
        self.head = new_head
        self.size -= 1
        return old_head

    def size(self):
        return self.size

    # return node containing val in list, if present, else None
    def search(self, node_name):
        temp = self.head
        while True:
            if temp.node_name == node_name:
                result = temp
                break
            else:
                if temp.node_next is None:
                    result = None
                    break
                else:
                    temp = temp.node_next
        return result

    # remove given node from list, node must be in list
    def remove(self, node_name):
        temp = self.head
        previous_node = None
        while True:
            if temp.node_name == node_name:
                remove_node = temp
                break
            else:
                if temp.node_next is None:
                    return "Node not in list"
                    break
                else:
                    # keep track of previous node so we can move pointer
                    previous_node = temp
                    temp = temp.node_next
        if remove_node:
            # removed node by changing pointers
            previous_node.node_next = remove_node.node_next
            self.size -= 1

    def printList(self):
        node = self.head
        return_str = '('
        while node.node_next is not None:
            return_str += node.node_name + ', '
            node = node.node_next
        return_str += node.node_name
        return_str += ')'
        print return_str
