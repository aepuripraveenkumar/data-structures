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
    node3 = Node(19)
    node4 = Node(18)
    myBST.insert(node1)
    myBST.insert(node2)
    myBST.insert(node3)
    myBST.insert(node4)
    assert node2.parent == node1
    assert node3.parent == node2
    assert node4.parent == node3

def test_balance_factor():
    myBST = balancedTree()
    node1 = Node(23)
    node2 = Node(21)
    node3 = Node(19)
    myBST.insert(node1)
    myBST.insert(node2)
    myBST.insert(node3)
    assert node1 == myBST.root
    assert node1.balanceFactor == 2