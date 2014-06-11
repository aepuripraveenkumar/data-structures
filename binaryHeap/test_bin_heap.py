import pytest
from binHeap import binHeap


def test_init_empty():
    """Tests that binHeap creates empty list on init"""
    work_bin = binHeap()
    assert len(work_bin.heapList) == 0


def test_init_iter():
    """Tests binHeap will perform binHeap sort upon accepting list1"""
    list1 = [1, 2, 3, 4]
    work_bin = binHeap(list1)
    assert work_bin.heapList == [4, 3, 2, 1]


def test_push_regular():
    """Tests binHeap correctly pushes value to binHeap"""
    test_list = [4, 3, 2, 1]
    work_bin = binHeap()
    work_bin.push(1)
    work_bin.push(2)
    work_bin.push(4)
    work_bin.push(3)
    assert work_bin.heapList == test_list


def test_push_duplicate():
    """Tests binHeap correctly pushes a duplicate list value to binHeap"""
    test_list = [4, 4, 2, 1, 3]
    work_bin = binHeap()
    work_bin.push(1)
    work_bin.push(4)
    work_bin.push(2)
    work_bin.push(3)
    work_bin.push(4)
    assert work_bin.heapList == test_list


def test_push_negValue():
    """Tests binHeap correctly pushes a negative value to binHeap"""
    test_list = [4, 4, 2, 1, 3, -1]
    work_bin = binHeap()
    work_bin.push(1)
    work_bin.push(4)
    work_bin.push(2)
    work_bin.push(3)
    work_bin.push(4)
    work_bin.push(-1)
    assert work_bin.heapList == test_list


def test_pop():
    """Tests binHeap correctly pops the head from the binHeap"""
    test_list = [4, 4, 2, 1, 3, -1]
    work_bin = binHeap(test_list)
    work_bin.pop()
    work_bin.pop()
    work_bin.pop()
    assert work_bin.heapList == [2, 1, -1]


def test_pop_empty():
    """Tests that pop on empty heapList raises an error"""
    work_bin = binHeap()
    with pytest.raises(IndexError):
        work_bin.pop()
