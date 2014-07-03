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

    def insert(self, value):
        """
        will insert the value val into the BST.  If val is already present, it will be ignored.
        """
        if not self.contains(value):
            if not self.root:
                self.root = value
        else:
            print "The tree doesnt need duplicate seeds"



    def contains(self, val):
        """
        Will return True if val is in BST, else False
        """
        if val in self.values:
            return True
        else:
            return False

    def size(self):
        """
        will return in size of the BST, equal to the number of
        values stored in the tree, 0 if tree is empty
        """
        pass

    def depth(self):
        """
        return an integer representing the total number of levels in
        tree.
        """
        pass

    def balance(self):
        """
        return an int, positive or negative that represents
        how well balanced the tree is. trees which are higher
        on the left than the right should return a positive value,
        trees which are higher on the right than the left should
        return a negative value. a truely balanced tree returns 0
        """
        pass