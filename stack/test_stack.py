from stack import Stack, Node
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
def test_stack_init():
    myStack = Stack()
    assert myStack.head is None


def test_stack_push():
    myStack = Stack()
    myStack.push("Bacon")
    myStack.push("Eggs")
    assert myStack.head.node_name == "Eggs"
    assert myStack.head.node_next.node_name == "Bacon"

def test_stack_pop():
    myStack = Stack()
    myStack.push("Bacon")
    myStack.push("Eggs")
    assert myStack.pop() == "Eggs"
    assert myStack.head.node_name == "Bacon"

def test_stack_empty_pop():
    myStack = Stack()
    assert myStack.pop() == "The stack is empty."