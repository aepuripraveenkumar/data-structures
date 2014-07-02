import bst


def test_add_node_root():
    myBST = bst.BST()
    myBST.add_node(23)

    assert myBST.root.value == 23


def test_add_node_children():
    myBST = bst.BST()
    myBST.add_node(23)
    myBST.add_node(10)
    myBST.add_node(50)

    assert myBST.root.left.value == 10
    assert myBST.root.right.value == 50
    assert myBST.root.left.parent == myBST.root
    assert myBST.root.right.parent == myBST.root
