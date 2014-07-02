class Node(object):
    def __init__(self, value, parent=None, left=None, right=None, level=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.level = level

    def __unicode__(self):
        return self.value


class BST(object):
    def __init__(self):
        self.root = None

    def add_node(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            current = self.root

            while True:
                if value <= current.value:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(value, parent=current)
                        break

                elif value > current.value:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(value, parent=current)
                        break

                else:
                    break
