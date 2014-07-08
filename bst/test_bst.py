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


def test_balanced_left():
    myBST = BST()
    node1 = Node(7)
    node2 = Node(4)
    node3 = Node(8)
    node4 = Node(10)
    node5 = Node(6)
    node6 = Node(2)
    myBST.insert(node1)
    myBST.insert(node2)
    myBST.insert(node3)
    myBST.insert(node4)
    myBST.insert(node5)
    myBST.insert(node6)
    assert myBST.balance(myBST.root) == 1


def test_balanced_right():
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
    assert myBST.balance(myBST.root) == -3


def test_balanced_balanced():
    myBST = BST()
    node1 = Node(7)
    node2 = Node(4)
    node3 = Node(8)
    node4 = Node(10)
    node5 = Node(6)
    node6 = Node(2)
    node7 = Node(9)
    myBST.insert(node1)
    myBST.insert(node2)
    myBST.insert(node3)
    myBST.insert(node4)
    myBST.insert(node5)
    myBST.insert(node6)
    myBST.insert(node7)
    assert myBST.balance(myBST.root) == 0


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


def test_breadth_first():
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
    generator = myBST.breadth_first(myBST.root)
    list1 = []
    for i in generator:
        list1.append(i)
    assert list1 == [20, 10, 23, 9, 18, 21]


def test_find_parent():
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
    assert myBST._find_node_parent(11) == node9


def test_del_leaf():
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
    assert node9.left == node10
    myBST.delete(11)
    assert myBST.contains(11) == False
    assert node9.left == None


def test_del_right_child():
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
    assert node9.left == node10
    myBST.delete(13)
    assert node8.left.value == 11


def test_del_two_children_left():
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
    myBST.delete(4)
    assert node2.value == 2
    assert node2.left is None


def test_del_two_children_right():
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
    myBST.delete(15)
    assert node8.value == 11

