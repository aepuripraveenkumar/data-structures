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

    def balance(self):
        """
        return an int, positive or negative that represents
        how well balanced the tree is. trees which are higher
        on the left than the right should return a positive value,
        trees which are higher on the right than the left should
        return a negative value. a truely balanced tree returns 0

        Add 1 to the number of nodes result to account for the starting node
        """

        if self.root.left:
            num_left_nodes = self.count_nodes(self.root.left) + 1
        else:
            num_left_nodes = 0
        if self.root.right:
            num_right_nodes = self.count_nodes(self.root.right) + 1
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

    def _has_2_children(self):
        has_2_children = False
        if self.left is not None:
            if self.right is not None:
                has_2_children = True
        return has_2_children

    def _find_node_in_order(self, node):
        visit_in_order = [node]
        for node in visit_in_order:
            if node.left:
                visit_in_order.append(node.left)
            if node.right:
                visit_in_order.append(node.right)
            yield node



    def _find_node_parent(self, value):
        generator = self._find_node_in_order(self.root)
        for i in generator:
            if i.right:
                if i.right.value == value:
                    return i
            if i.left:
                if i.left.value == value:
                    return i


    def delete(self, val):
        if not self.contains(val):
            return
        delete_node_parent = self._find_node_parent(val)
        if delete_node_parent.left.value == val:
            if self._is_leaf(delete_node_parent):
                delete_node_parent.left = None
            else:
                delete_node_parent.right = None
            self.values.remove(val)


if __name__ == "__main__":
    myBST = BST()
    node1 = Node(20)
    node2 = Node(23)
    node3 = Node(10)
    node4 = Node(18)
    node5 = Node(9)
    node6 = Node(21)
    myBST.insert(node1)
    myBST.insert(node2)
    myBST.insert(node3)
    myBST.insert(node4)
    myBST.insert(node5)
    myBST.insert(node6)
    generator = myBST._find_node_in_order(myBST.root)
    for i in generator:
        print i
