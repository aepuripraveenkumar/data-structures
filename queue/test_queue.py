from queue import Queue, Node
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


# test initialization of queue, size should be 0
def test_stack_init():
    myQueue = Queue()
    assert myQueue.head is None
    assert myQueue.tail is None
    assert myQueue.size == 0


def test_stack_enqueue():
    myQueue = Queue()
    myQueue.enqueue("Bacon")
    myQueue.enqueue("Eggs")
    myQueue.enqueue("Coffee")
    assert myQueue.tail.node_name == "Coffee"
    assert myQueue.tail.next_node == None
    assert myQueue.head.node_name == "Bacon"
    assert myQueue.head.node_next.node_name == "Eggs"
    assert myQueue.head.node_next.node_next == "Coffee"


def test_stack_dequeue():
    myQueue = Queue()
    myQueue.enqueue("Bacon")
    myQueue.enqueue("Eggs")
    myQueue.enqueue("Coffee")
    myQueue.enqueue("Ham")
    myQueue.enqueue("Hash")
    myQueue.enqueue("OJ")
    return_value = myQueue.dequeue()
    assert myQueue.tail.node_name == "OJ"
    assert myQueue.tail.next_node == None
    assert myQueue.head.node_name == "Bacon"
    assert myQueue.head.node_next.node_name == "Eggs"
    assert myQueue.head.node_next.node_next == "Coffee"
    assert return_value == "Bacon"
    assert myQueue.tail.node_name == "OJ"
    assert myQueue.tail.next_node == None
    assert myQueue.head.node_name == "Eggs"
    assert myQueue.head.node_next.node_name == "Coffee"
    assert myQueue.head.node_next.node_next == "Ham"

def test_stack_size():
    myQueue = Queue()
    myQueue.enqueue("Bacon")
    myQueue.enqueue("Eggs")
    myQueue.enqueue("Coffee")
    assert myQueue.size == 3
    myQueue.dequeue()
    assert myQueue.size == 2
    myQueue.dequeue()
    assert myQueue.size == 1
    myQueue.dequeue()
    assert myQueue.size == 0

def test_stack_empty_dequeue():
    myQueue = Queue()
    assert myQueue.dequeue() is Exception
