import random
import time
import pylab


def merge_sort(uList):
    """
    implementation of merge_sort
    n*logn
    """

    # base case, list of zero or one elements is sorted
    if len(uList) <= 1:
        return uList

    # divide list into equal sized sublists
    left, right = [], []
    middle = len(uList) / 2
    for x in uList[:middle]:
        left.append(x)
    for x in uList[middle:]:
        right.append(x)

    # recursively sort both sublists
    left = merge_sort(left)
    right = merge_sort(right)

    # merge sorted sublists
    return _merge(left, right)


def _merge(left, right):
    result = []
    # assign element of sublists to result until no element to merge
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            # compare first two elemnts, which is the small one
            # of each sublist
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result

if __name__ == '__main__':
    results = []
    ranges = [10, 100, 1000]
    for t in ranges:
        for i in range(100):
            list2 = [random.randint(1, 100) for i in range(t)]
            start = time.time()
            merge_sort(list2)
            end = time.time()
            results.append(end-start)
    pylab.figure(1)
    p1, = pylab.plot([i for i in range(100)], results[0:100])
    p2, = pylab.plot([i for i in range(100)], results[100:200])
    p3, = pylab.plot([i for i in range(100)], results[200:])
    pylab.show()
