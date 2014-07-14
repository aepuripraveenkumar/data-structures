from bst import Node, BST


class Node(object):
    def __init__(self, value, parent=None, left=None, right=None, level=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.balanceFactor = 0

    def __unicode__(self):
        return self.value

    def isLeftChild(self):
        return self.parent and self.parent.left == self

    def isRightChild(self):
        return self.parent and self.parent.right == self

    def isLeaf(self):
        return not (self.right or self.left)

    def hasAnyChildren(self):
        return self.right or self.left

    def hasBothChildren(self):
        return self.right and self.left


class BST(object):
    def __init__(self):
        self.root = None
        self.values = []

    def insert(self, new):
        """
        will insert the value val into the BST.
        If val is already present it will be ignored.
        """
        if not self.contains(new.value):
            if not self.root:
                self.root = new
                self.values.append(new.value)
            else:
                inserting = True
                top = self.root
                while inserting:
                    if new.value < top.value:
                        if top.left:
                            top = top.left
                        else:
                            new.parent = top
                            top.left = new
                            self.values.append(new.value)
                            # set balance factor of parents
                            inserting = False
                    else:
                        if top.right:
                            top = top.right
                        else:
                            new.parent = top
                            top.right = new
                            self.values.append(new.value)
                            inserting = False
        else:
            raise ValueError("The tree doesnt need duplicate seeds")

    def contains(self, value):
        """
        Will return True if val is in BST, else False
        """
        if value in self.values:
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

        right_depth = []
        left_depth = []
        if self.root.right:
            right = self.in_order(self.root.right)
            for i in right:
                right_weight.append(i)
        if self.root.left:
            left = self.in_order(self.root.left)
            for i in left:
                left_weight.append(i)

        if len(right_depth) > len(left_depth):
            return len(right_depth)
        else:
            return len(left_depth)


        return self.depth

    def balance(self, node=None):
        """
        return an int, positive or negative that represents
        how well balanced the tree is. trees which are higher
        on the left than the right should return a positive value,
        trees which are higher on the right than the left should
        return a negative value. a truely balanced tree returns 0

        Add 1 to the number of nodes result to account for the starting node
        """
        right_weight = []
        left_weight = []
        if self.root.right:
            right = self.in_order(self.root.right)
            for i in right:
                right_weight.append(i)
        if self.root.left:
            left = self.in_order(self.root.left)
            for i in left:
                left_weight.append(i)
        balance = len(left_weight) - len(right_weight)
        if balance > 0:
            return 1
        elif balance < 0:
            return -1
        else:
            return 0

    def count_nodes(self, start, count=0):
        """
        Recursion algorithm that travels to the last node of each left branch
        of the tree passed to it.  As it returns, it adds one for
        a left branch and then travels down the right branch for that node and
        adds one for each node.
        """

        if start.left:
            count += self.count_nodes(start.left) + 1
        if start.right:
            count += self.count_nodes(start.right) + 1
        return count

    def pre_order(self, node):
        """
        return a generator that will return the values in the tree using
        pre-order traversal, one at a time.
        """
        # base case
        if node is None:
            return
        else:
            yield node.value
            for n in self.pre_order(node.left):
                yield n
            for n in self.pre_order(node.right):
                yield n

    def in_order(self, node):
        """
        return a generator that will return the values in the tree using
        in-order traversal, one at a time.
        """
        # base case
        if node is None:
            return
        else:
            for n in self.in_order(node.left):
                yield n
            yield node.value
            for n in self.in_order(node.right):
                yield n

    def post_order(self, node):
        """
        return a generator that will return the values in the tree using
        post_order traversal, one at a time.
        """
        # base case
        if node is None:
            return
        else:
            for n in self.post_order(node.left):
                yield n
            for n in self.post_order(node.right):
                yield n
            yield node.value

    def breadth_first(self, node):
        """
        return a generator that will return the values in the tree using a
        breadth-first search
        """
        visit_in_order = [node]
        for node in visit_in_order:
            if node.left:
                visit_in_order.append(node.left)
            if node.right:
                visit_in_order.append(node.right)
            yield node.value

    def _is_leaf(self, node):
        is_leaf = False
        if node.left is None:
            if node.right is None:
                is_leaf = True
        return is_leaf

    def _find_node_breadth(self, node):
        visit_in_order = [node]
        for node in visit_in_order:
            if node.left:
                visit_in_order.append(node.left)
            if node.right:
                visit_in_order.append(node.right)
            yield node

    def _find_node(self, value):
        generator = self._find_node_breadth(self.root)
        for i in generator:
            if i.right:
                if i.right.value == value:
                    return i.right
            if i.left:
                if i.left.value == value:
                    return i.left

    def _delete_the_node(self, delete_node):
        generator = None
        print "Function value: ", delete_node.value
        print "Function left: ", delete_node.left
        if delete_node.left or delete_node.right:
            print "create generator"
            generator = self._find_node_breadth(delete_node)
        if delete_node.parent.left == delete_node:
            delete_node.parent.left = None
        else:
            delete_node.parent.right = None
        if generator:
            for i in generator:
                if i is not delete_node:
                    i.left = None
                    i.right = None
                    i.parent = None
                    self.insert(i)

    def _remove_child(self, delete_node):
        replace_node = Node(None)
        generator = self._find_node_breadth(delete_node)
        for i in generator:
            if i.value > replace_node.value:
                replace_node = i
        # if only a left child on delete node
        if replace_node == delete_node:
            replace_node = delete_node.left
        # set input node to biggest value
        delete_node.value = replace_node.value
        # delete moved node
        print "Replace node value: ", replace_node.value
        print "Replace node left: ", replace_node.left
        self._delete_the_node(replace_node)

    def delete(self, val):
        if not self.contains(val):
            return
        # get the node we are trying to delete
        delete_node = self._find_node(val)
        is_deleted = False

        while not is_deleted:
            if self._is_leaf(delete_node):
                self._delete_the_node(delete_node)
                is_deleted = True

            else:
                self._remove_child(delete_node)
                is_deleted = True

        self.values.remove(val)


class balancedTree(BST):

    def insert(self, new):
        """
        will insert the value val into the BST.
        If val is already present it will be ignored.
        """
        if not self.contains(new.value):
            if not self.root:
                self.root = new
                self.values.append(new.value)
            else:
                inserting = True
                top = self.root
                while inserting:
                    if new.value < top.value:
                        if top.left:
                            top = top.left
                        else:
                            new.parent = top
                            top.left = new
                            self.values.append(new.value)
                            # set balance factor of parents
                            self.updateBalance(new)
                            inserting = False
                    else:
                        if top.right:
                            top = top.right
                        else:
                            new.parent = top
                            top.right = new
                            self.values.append(new.value)
                            # update balance factor of parents
                            self.updateBalance(new)
                            inserting = False
        else:
            raise ValueError("The tree doesnt need duplicate seeds")

    def updateBalance(self, node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent != None:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1

            if node.parent.balanceFactor != 0:
                self.updateBalance(node.parent)

    def rebalance(self, node):
        pass

    def rotateLeft(self, rotRoot):
        # the new root will be the rotating node's right child
        newRoot = rotRoot.right
        # set old root's right to new root's left
        rotRoot.right = newRoot.left
        # clean up parent pointers
        if newRoot.left != None:
            newRoot.left.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if self.root = rotRoot:
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.left = newRoot
            else:
                rotRoot.parent.right = newRoot
        # update new root pointers
        newRoot.left = rotRoot
        newRoot.parent = newRoot
        # update balance factors
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 - max(rotRoot.balanceFactor, 0)

    def rotateRight(self, rotRoot):
        # need to fix
        # the new root will be the rotating node's left child
        newRoot = rotRoot.left
        # set old root's left to new root's right
        rotRoot.left = newRoot.right
        # clean up parent pointers
        if newRoot.right != None:
            newRoot.right.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if self.root = rotRoot:
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.left = newRoot
            else:
                rotRoot.parent.right = newRoot
        # update new root point
        newRoot.right = rotRoot
        # update
        rotRoot.parent = newRoot
        # update balance factors
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 - max(rotRoot.balanceFactor, 0)
