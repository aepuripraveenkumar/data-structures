

class No_Node_Exception(Exception):
    pass


class Node(object):
    def __init__(self, node_name=None, node_next=None):
        self.node_name = node_name
        self.node_next = node_next


class Linked_List(object):
    def __init__(self):
        self.size = 0
        self.head = None

    def __str__(self):
        statement = []
        if not self.size:
            statement = tuple(statement)
            return str(statement)
        temp = self.head
        while temp:
            statement.append(temp.node_name)
            temp = temp.node_next
        statement = tuple(statement)
        return str(statement)

    # insert node at head
    def insert(self, node_name):
        # the new head should point to the old head
        if not self.head:
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
                if not temp.node_next:
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
                if not temp.node_next:
                    raise No_Node_Exception("-1")
                else:
                    # keep track of previous node so we can move pointer
                    previous_node = temp
                    temp = temp.node_next
        if remove_node and remove_node != self.head:
            # removed node by changing pointers
            previous_node.node_next = remove_node.node_next
            self.size -= 1
        else:
            self.head = self.head.node_next
