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


def test_depth_tricky():
    myBST = BST()
    node1 = Node(10)
    node2 = Node(9)
    node3 = Node(8)
    node4 = Node(7)
    node5 = Node(6)
    node6 = Node(11)
    myBST.insert(node1)
    myBST.insert(node2)
    myBST.insert(node3)
    myBST.insert(node4)
    myBST.insert(node5)
    myBST.insert(node6)
    assert myBST.depth == 5


def test_pre_order():
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
    generator = myBST.pre_order(myBST.root)
    list1 = []
    for i in generator:
        list1.append(i)
    assert list1 == [20, 10, 9, 18, 23, 21]


def test_in_order():
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
    generator = myBST.in_order(myBST.root)
    list1 = []
    for i in generator:
        list1.append(i)
    assert list1 == [9, 10, 18, 20, 21, 23]


def test_post_order():
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
    generator = myBST.post_order(myBST.root)
    list1 = []
    for i in generator:
        list1.append(i)
    assert list1 == [9, 18, 10, 21, 23, 20]
