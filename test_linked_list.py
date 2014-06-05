import pytest
from linked_list import Node
from linked_list import Linked_List
from linked_list import insert
from linked_list import pop
from linked_list import size
from linked_list import search
from linked_list import remove
#from linked_list import print


def test_node_create():
    a = Node("One")

    assert(a.value == "One")


def test_linked_list():
    my_list = Linked_List()
    my_list.start = Node("One")

    assert(my_list.start.value == "One")
    assert(my_list.start.next_node == None)


def test_insert():
    my_list = Linked_List()
    my_list.insert("One")
    my_list.insert("Two")
    my_list.insert(3)
    ptr = my_list.start

    assert(ptr.value == "One")
    ptr = ptr.next_node
    assert(ptr.value == "Two")
    ptr = ptr.next_node
    assert(ptr.value == 3)

