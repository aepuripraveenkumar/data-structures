import pytest
from bin_heap import BinHeap


def test_init_empty():
    """Tests that BinHeap creates empty list on init"""
    work_bin = BinHeap()
    assert len(work_bin.heap_list) == 0


def test_init_iter():
    """Tests BinHeap will perform BinHeap sort upon accepting list1"""
    list1 = [1, 2, 3, 8]
    work_bin = BinHeap(list1)
    assert work_bin.heap_list == [8, 3, 2, 1]


def test_push_regular():
    """Tests BinHeap correctly pushes value to BinHeap"""
    test_list = [4, 3, 2, 1]
    work_bin = BinHeap()
    work_bin.push(1)
    work_bin.push(2)
    work_bin.push(4)
    work_bin.push(3)
    assert work_bin.heap_list == test_list


def test_push_duplicate():
    """Tests BinHeap correctly pushes a duplicate list value to BinHeap"""
    test_list = [4, 4, 2, 1, 3]
    work_bin = BinHeap()
    work_bin.push(1)
    work_bin.push(4)
    work_bin.push(2)
    work_bin.push(3)
    work_bin.push(4)
    assert work_bin.heap_list == test_list


def test_push_negValue():
    """Tests BinHeap correctly pushes a negative value to BinHeap"""
    test_list = [4, 4, 2, 1, 3, -1]
    work_bin = BinHeap()
    work_bin.push(1)
    work_bin.push(4)
    work_bin.push(2)
    work_bin.push(3)
    work_bin.push(4)
    work_bin.push(-1)
    assert work_bin.heap_list == test_list


def test_pop():
    """Tests BinHeap correctly pops the head from the BinHeap"""
    test_list = [4, 4, 2, 1, 3, -1]
    work_bin = BinHeap(test_list)
    work_bin.pop()
    work_bin.pop()
    work_bin.pop()
    assert work_bin.heap_list == [2, -1, 1]


def test_pop_empty():
    """Tests that pop on empty heap_list raises an error"""
    work_bin = BinHeap()
    with pytest.raises(IndexError):
        work_bin.pop()
