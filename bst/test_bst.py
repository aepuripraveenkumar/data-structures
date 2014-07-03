from bst import Node, BST


def test_add_node_root():
    myBST = BST()
    node1 = Node(23)
    myBST.insert(node1.value)

    assert myBST.root == 23
