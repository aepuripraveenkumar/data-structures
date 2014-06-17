from graph import Node


def test_init_node():
    newNode = Node("Decatur")
    assert newNode.value == "Decatur"
