import quicksort
import random


def test_insertion_sort():
    item_size = [1000]
    for i in item_size:
        unsorted = [random.randint(0, i) for j in range(i)]
        quicksort.quicksort(unsorted, 0, 999)
    while i < len(item_size):
        assert unsorted[i] < unsorted[i + 1]
        i += 1
