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
        if not self.contains(new.value):
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
                            new.parent = top
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
                            new.parent = top
                            top.right = new
                            self.values.append(new.value)
                            self.temp_depth += 1
                            if self.temp_depth > self.depth:
                                self.depth = self.temp_depth
                            inserting = False
        else:
            print "The tree doesnt need duplicate seeds"
            raise ValueError

    def contains(self, value):
        """
        Will return True if val is in BST, else False
        """
        if value in self.values:
            return True
        else:
            return False
        # top = self.root
        # if Node.value == top.value:
        #     return True
        # elif Node.value < top.value:
        #     top = top.left

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

    def balance(self, node=None):
        """
        return an int, positive or negative that represents
        how well balanced the tree is. trees which are higher
        on the left than the right should return a positive value,
        trees which are higher on the right than the left should
        return a negative value. a truely balanced tree returns 0

        Add 1 to the number of nodes result to account for the starting node
        """

        if node.left:
            num_left_nodes = self.count_nodes(node.left) + 1
        else:
            num_left_nodes = 0
        if node.right:
            num_right_nodes = self.count_nodes(node.right) + 1
        else:
            num_right_nodes = 0
        return num_left_nodes - num_right_nodes

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


if __name__ == "__main__":
    myBST = BST()
    node1 = Node(7)
    node2 = Node(4)
    node3 = Node(8)
    node4 = Node(10)
    node5 = Node(6)
    node6 = Node(2)
    node7 = Node(9)
    node8 = Node(15)
    node9 = Node(13)
    node10 = Node(11)
    node11 = Node(20)
    node12 = Node(23)
    node13 = Node(19)
    myBST.insert(node1)
    myBST.insert(node2)
    myBST.insert(node3)
    myBST.insert(node4)
    myBST.insert(node5)
    myBST.insert(node6)
    myBST.insert(node7)
    myBST.insert(node8)
    myBST.insert(node9)
    myBST.insert(node10)
    myBST.insert(node11)
    myBST.insert(node12)
    myBST.insert(node13)
    myBST.delete(4)
    generator = myBST._find_node_breadth(myBST.root)
    for i in generator:
        print i.value
