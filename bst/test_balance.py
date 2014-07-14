from balance_tree import balancedTree, Node


def test_add_node_root():
    myBST = balancedTree()
    node1 = Node(23)
    myBST.insert(node1)

    assert myBST.root.value == 23
    assert myBST.size() == 1


def test_parent():
    myBST = balancedTree()
    node1 = Node(23)
    node2 = Node(21)
    myBST.insert(node1)
    myBST.insert(node2)
    assert node2.parent == node1


def test_easy_balance_factor():
    myBST = balancedTree()
    node1 = Node(23)
    node2 = Node(24)
    node3 = Node(19)
    myBST.insert(node1)
    myBST.insert(node2)
    myBST.insert(node3)
    assert myBST.root.balanceFactor == 0


def test_hard_balance_factor():
    myBST = balancedTree()
    node1 = Node(23)
    node2 = Node(24)
    node3 = Node(18)
    node4 = Node(27)
    node5 = Node(2)
    node6 = Node(65)
    myBST.insert(node1)
    myBST.insert(node2)
    myBST.insert(node3)
    myBST.insert(node4)
    myBST.insert(node5)
    myBST.insert(node6)
    assert myBST.root.balanceFactor == 0
