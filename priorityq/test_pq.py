import pytest
from pq import PriorityQ


def test_init():
    """Tests that BinHeap creates empty list on init"""
    work_pq = PriorityQ()
    assert len(work_pq.priority_q) == 0


def test_insert():
    """Tests PriorityQ will perform insert"""
    work_pq = PriorityQ()
    work_pq.insert(78, "This is priority 78.")
    assert work_pq.priority_q[0].priority == 78
    assert work_pq.priority_q[0].message =="This is priority 78."

def test_insert_swap():
    """Tests PriorityQ will perform insert and swap highest priority to
    top"""
    work_pq = PriorityQ()
    work_pq.insert(78, "This is priority 78.")
    work_pq.insert(80, "This is priority 80.")
    work_pq.insert(78, "This is priority 78-2.")
    work_pq.insert(5, "This is priority 5.")
    work_pq.insert(25, "This is priority 25.")
    work_pq.insert(97, "This is priority 97.")
    assert work_pq.priority_q[0].priority == 97
    assert work_pq.priority_q[0].message == "This is priority 97."


def test_push_peek():
    """Tests PriorityQ correctly pushes value to PriorityQ"""
    work_pq = PriorityQ()
    work_pq.insert(78, "This is priority 78.")
    work_pq.insert(80, "This is priority 80.")
    work_pq.insert(78, "This is priority 78-2.")
    work_pq.insert(5, "This is priority 5.")
    work_pq.insert(25, "This is priority 25.")
    work_pq.insert(97, "This is priority 97.")
    assert work_pq.peek() == "97 -- This is priority 97."



def test_pop():
    """Tests PriorityQ correctly pops the head from the PriorityQ"""
    work_pq = PriorityQ()
    work_pq.insert(78, "This is priority 78.")
    work_pq.insert(80, "This is priority 80.")
    work_pq.insert(78, "This is priority 78-2.")
    work_pq.insert(5, "This is priority 5.")
    work_pq.insert(25, "This is priority 25.")
    work_pq.insert(97, "This is priority 97.")
    work_pq.pop()
    assert work_pq.priority_q[0].priority == 80
    assert work_pq.priority_q[0].message == "This is priority 80."



def test_pop_empty():
    """Tests that pop on empty heap_list raises an error"""
    work_pq = PriorityQ()
    with pytest.raises(IndexError):
        work_pq.pop()
