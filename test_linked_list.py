from linked_list import Node, Linked_List
import pytest


# test init name of Node
def test_node_init_name():
    node = Node('Polly')
    assert node.node_name == "Polly"


# test node_next of Node object
def test_node_init_next():
    node1 = Node('Polly')
    node2 = Node("Jane", node1)
    assert node2.node_next == node1


# test initialization of Linked_List, size should be 0
def test_list_init():
    list1 = Linked_List()
    assert list1.size == 0
    assert list1.head is None


def test_list_head_when_none():
    list1 = Linked_List()
    list1.insert("Mary")
    assert list1.head.node_name == "Mary"
    assert list1.size == 1
    assert list1.head.node_next is None


def test_list_head_two_nodes():
    list1 = Linked_List()
    list1.insert("Mary")
    list1.insert("Kyle")
    assert list1.size == 2
    assert list1.head.node_name == "Kyle"
    assert list1.head.node_next.node_name == "Mary"


def test_pop():
    list1 = Linked_List()
    list1.insert("John")
    list1.insert("Paul")
    list1.insert("George")
    list1.insert("Ringo")
    popped = list1.pop()
    assert popped.node_name == "Ringo"
    assert list1.head.node_name == "George"
    assert list1.size == 3


def test_next():
    list1 = Linked_List()
    list1.insert("John")
    list1.insert("Paul")
    list1.insert("George")
    list1.insert("Ringo")
    assert list1.head.node_next.node_next.node_next.node_name == "John"


def test_regular_search():
    list1 = Linked_List()
    list1.insert("John")
    list1.insert("Paul")
    list1.insert("George")
    list1.insert("Ringo")
    searched_node = list1.search("George")
    assert searched_node.node_name == "George"
    searched_node = list1.search("John")
    assert searched_node.node_name == "John"
    searched_node = list1.search("Ralph")
    assert searched_node is None


def test_remove():
    list1 = Linked_List()
    list1.insert("John")
    list1.insert("Paul")
    list1.insert("George")
    list1.insert("Ringo")
    list1.remove("John")
    assert list1.head.node_next.node_next.node_next is None
    list1.remove("George")
    assert list1.size == 2
    assert list1.head.node_next.node_name == "Paul"
    assert list1.remove("Pete") == "Node not in list"


def test_print():
    list1 = Linked_List()
    list1.insert("John")
    list1.insert("Paul")
    list1.insert("George")
    list1.insert("Ringo")
    list1.remove("John")
    assert print list1
