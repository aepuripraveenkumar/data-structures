import random
import time
import sys


def quicksort(list_u, first, last):
    if first < last:
        p = partition(list_u, first, last)
        quicksort(list_u, first, p - 1)
        quicksort(list_u, p + 1, last)
    return list_u


def partition(list_u, first, last):
    pivot = list_u[first]
    left = first + 1
    right = last
    done = False

    while not done:
        while left <= right and list_u[left] <= pivot:
            left += 1
        while list_u[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            done = True
        else:
            list_u[left], list_u[right] = list_u[right], list_u[left]
    list_u[first], list_u[right] = list_u[right], list_u[first]
    return right

if __name__ == "__main__":
    sys.setrecursionlimit(20000)
    item_size = [1000, 10000]
    for i in item_size:
        unsorted = [random.randint(0, i) for j in range(i)]
        start_time = time.time()
        quicksort(unsorted, 0, i-1)
        end_time = time.time()
        total = end_time - start_time
        print "Random sort for %i items took %f" % (i, total)
        start_time = time.time()
        quicksort(unsorted, 0, i-1)
        end_time = time.time()
        total = end_time - start_time
        print "Best case sort for %i items took %f" % (i, total)
        unsorted.sort(reverse=True)
        start_time = time.time()
        quicksort(unsorted, 0, i-1)
        end_time = time.time()
        total = end_time - start_time
        print "Worst case sort for %i items took %f" % (i, total)
