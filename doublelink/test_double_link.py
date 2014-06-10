from double_link import Node, Double_list
import pytest


# test init name of Node
def test_node_init_name():
    node = Node('Polly')
    assert node.node_name == "Polly"
    assert node.node_next is None
    assert node.node_prev is None


# test node_next of Node object
def test_node_init_next_prev():
    node1 = Node('Polly')
    node2 = Node("Jane", node1)
    assert node2.node_next == node1


def test_insert():
    dList = Double_list()
    dList.insert("Harry")
    assert dList.list_ptr.node_name == "Harry"
    dList.insert("Ron")
    assert dList.list_ptr.node_name == "Ron"
    assert dList.list_ptr.node_next.node_name == "Harry"
    assert dList.list_ptr.node_next.node_prev.node_name == "Ron"
    dList.insert("Snape")
    middle_node = dList.list_ptr.node_next
    assert middle_node.node_prev.node_name == "Snape"
    assert middle_node.node_next.node_name == "Harry"


def test_append():
    dList = Double_list()
    dList.insert("Harry")
    dList.insert("Ron")
    dList.append("Snape")
    assert dList.list_ptr.node_next.node_name == "Harry"
    middle_node = dList.list_ptr.node_next
    assert middle_node.node_next.node_name == "Snape"
    assert middle_node.node_next.node_next is None
    assert middle_node.node_next.node_prev.node_name == "Harry"


def test_pop():
    dList = Double_list()
    dList.insert("Harry")
    dList.insert("Ron")
    dList.append("Snape")
    assert dList.pop() == "Ron"
    assert dList.list_ptr.node_name == "Harry"
    assert dList.list_ptr.node_prev is None
    assert dList.list_ptr.node_next.node_name == "Snape"


def test_shift():
    dList = Double_list()
    dList.insert("Harry")
    dList.insert("Ron")
    dList.append("Snape")
    assert dList.shift() == "Snape"
    assert dList.list_ptr.node_next.node_next is None


def test_remove():
    dList = Double_list()
    dList.insert("Harry")
    dList.insert("Ron")
    dList.append("Snape")
    dList.remove("Harry")
    assert dList.list_ptr.node_next.node_name == "Snape"
    assert dList.list_ptr.node_next.node_prev.node_name == "Ron"


def test_empty():
    dList = Double_list()
    with pytest.raises(AttributeError):
        dList.remove("Penguins")
