import radixsort
import random


def test_radix_sort():
    item_size = [1000]
    for i in item_size:
        unsorted = [random.randint(0, i) for j in range(i)]
        radixsort.radix_sort(unsorted)
    while i < len(item_size):
        assert unsorted[i] < unsorted[i + 1]
        i += 1


def test_radix_str_sort():
    my_list = ['z', 'car', 'horse', 'whale', 'antelope', 'dog', 'cat']
    sorted = radixsort.radix_sort(my_list)
    assert sorted == ['antelope', 'car', 'cat', 'dog', 'horse', 'whale', 'z']
