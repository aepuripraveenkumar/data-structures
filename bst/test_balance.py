from balance_tree import balancedTree, Node

def test_add_node_root():
    myBST = balancedTree()
    node1 = Node(23)
    myBST.insert(node1)

    assert myBST.root.value == 23
    assert myBST.size() == 1