from bst import Node, BST
import pytest


def test_add_node_root():
    myBST = BST()
    node1 = Node(23)
    myBST.insert(node1)

    assert myBST.root.value == 23
    assert myBST.size() == 1


def test_add_node_root_negative():
    myBST = BST()
    node1 = Node(23)
    node2 = Node(25)
    myBST.insert(node1)
    myBST.insert(node2)

    assert myBST.root.value == 23
    assert myBST.size() == 2


def test_add_node_root_right():
    myBST = BST()
    node1 = Node(23)
    node2 = Node(25)
    myBST.insert(node1)
    myBST.insert(node2)

    assert myBST.root.right.value == 25


def test_second_level_right():
    myBST = BST()
    node1 = Node(23)
    node2 = Node(50)
    node3 = Node(55)
    myBST.insert(node1)
    myBST.insert(node2)
    myBST.insert(node3)

    assert node2.right.value == 55
    assert myBST.size() == 3


def test_add_node_left():
    myBST = BST()
    node1 = Node(23)
    node2 = Node(12)
    myBST.insert(node1)
    myBST.insert(node2)

    assert node1.left.value == 12
    assert myBST.size() == 2


def test_second_level_left():
    myBST = BST()
    node1 = Node(23)
    node2 = Node(12)
    node3 = Node(18)
    myBST.insert(node1)
    myBST.insert(node2)
    myBST.insert(node3)

    assert node2.right.value == 18
    assert myBST.size() == 3


def test_duplicate():
    myBST = BST()
    node1 = Node(23)
    node2 = Node(12)
    node3 = Node(12)
    myBST.insert(node1)
    myBST.insert(node2)
    with pytest.raises(ValueError):
        myBST.insert(node3)


def test_depth_easy():
    myBST = BST()
    node1 = Node(23)
    node2 = Node(12)
    node3 = Node(14)
    node4 = Node(8)
    node5 = Node(1)
    myBST.insert(node1)
    myBST.insert(node2)
    myBST.insert(node3)
    myBST.insert(node4)
    myBST.insert(node5)
    assert myBST.depth == 4