from linked_list import Node, Linked_List
import pytest


# test init name of Node
def test_node_init_name():
    node = Node('Polly')
    assert node.name == "Polly"


# test next of Node object
def test_node_init_next():
    node1 = Node('Polly')
    node2 = Node("Jane", node1)
    assert node2.next == node1


# test initialization of Linked_List, size should be 0
def test_list_init():
    list1 = Linked_List()
    assert list1.size == 0


def test_list_head_when_none():
    list1 = Linked_List()
    list1.insert("Mary")
    assert list1.head.name == "Mary"
    assert list1.size == 1


def test_list_head_two_nodes():
    list1 = Linked_List()
    list1.insert("Mary")
    list1.insert("Kyle")
    assert list1.size == 2
    assert list1.head.name == "Kyle"
    assert list1.head.next.name == "Mary"


def test_pop():
    list1 = Linked_List()
    list1.insert("John")
    list1.insert("Paul")
    list1.insert("George")
    list1.insert("Ringo")
    popped = list1.pop()
    assert popped.name == "Ringo"
    assert list1.head.name == "George"
    assert list1.size == 3


def test_next():
    list1 = Linked_List()
    list1.insert("John")
    list1.insert("Paul")
    list1.insert("George")
    list1.insert("Ringo")
    assert list1.head.next.next.next.name == "John"


def test_regular_search():
    list1 = Linked_List()
    list1.insert("John")
    list1.insert("Paul")
    list1.insert("George")
    list1.insert("Ringo")
    searched_node = list1.search("George")
    assert searched_node.name == "George"












