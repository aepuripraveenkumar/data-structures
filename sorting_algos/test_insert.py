import pytest
from insert_sort import insertionSort
import random


# test init name of Node
def test_insertion():
    list1 = [random.randint(1, 100) for i in range(100)]
    list2 = list1[:]
    list3 = list1[:]
    insertionSort(list2)
    assert list2 == sorted(list3)
