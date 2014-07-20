import pytest
from insert_sort import insertionSort
from merge_sort import merge_sort, _merge
from quick_sort1 import quicksort, partition
import random


# test init name of Node
def test_insertion():
    list1 = [random.randint(1, 100) for i in range(100)]
    list2 = list1[:]
    list3 = list1[:]
    insertionSort(list2)
    assert list2 == sorted(list3)


def test_merge():
    list1 = [random.randint(1, 100) for i in range(100)]
    list2 = list1[:]
    list3 = list1[:]
    list2 = merge_sort(list2)
    assert list2 == sorted(list3)


def test_quick():
    list1 = [random.randint(1, 100) for i in range(100)]
    list2 = list1[:]
    list3 = list1[:]
    list2 = quicksort(list2, 0, len(list2)-1)
    assert list2 == sorted(list3)

