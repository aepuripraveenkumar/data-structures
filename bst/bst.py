class Node(object):
    def __init__(self, value, parent=None, left=None, right=None, level=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __unicode__(self):
        return self.value


class BST(object):
    def __init__(self):
        self.root = None
        self.values = []
        self.depth = 0

    def insert(self, new):
        """
        will insert the value val into the BST.
        If val is already present it will be ignored.
        """
        if not self.contains(new):
            self.temp_depth = 1
            if not self.root:
                self.root = new
                self.values.append(new.value)
                self.depth += 1
            else:
                inserting = True
                top = self.root
                while inserting:
                    if new.value < top.value:
                        if top.left:
                            top = top.left
                            self.temp_depth += 1
                        else:
                            top.left = new
                            self.values.append(new.value)
                            self.temp_depth += 1
                            if self.temp_depth > self.depth:
                                self.depth = self.temp_depth
                            inserting = False
                    else:
                        if top.right:
                            top = top.right
                            self.temp_depth += 1
                        else:
                            top.right = new
                            self.values.append(new.value)
                            self.temp_depth += 1
                            if self.temp_depth > self.depth:
                                self.depth = self.temp_depth
                            inserting = False
        else:
            print "The tree doesnt need duplicate seeds"
            raise ValueError

    def contains(self, Node):
        """
        Will return True if val is in BST, else False
        """
        if Node.value in self.values:
            return True
        else:
            return False

    def size(self):
        """
        will return in size of the BST, equal to the number of
        values stored in the tree, 0 if tree is empty
        """
        return len(self.values)

    def depth(self):
        """
        return an integer representing the total number of levels in
        tree.
        """
        return self.depth

    def balance(self):
        """
        return an int, positive or negative that represents
        how well balanced the tree is. trees which are higher
        on the left than the right should return a positive value,
        trees which are higher on the right than the left should
        return a negative value. a truely balanced tree returns 0
        """
        pass