import random
# import pylab
import time


def quicksort(uList, start, end):
    if start < end:
        # partition the list
        pivot = partition(uList, start, end)
        # sort both halves
        quicksort(uList, start, pivot-1)
        quicksort(uList, pivot+1, end)
    return uList


def partition(uList, start, end):
    pivot = uList[start]
    left = start+1
    right = end
    done = False
    while not done:
        # increase left until it is bigger than pivot or smaller than right
        while left <= right and uList[left] <= pivot:
            left = left + 1
        # until right is less than pivot
        while uList[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            # swap places
            temp = uList[left]
            uList[left] = uList[right]
            uList[right] = temp
    # swap start with uList[right]
    temp = uList[start]
    uList[start] = uList[right]
    uList[right] = temp
    return right


# if __name__ == '__main__':
#     results = []
#     ranges = [10, 100, 1000]
#     for t in ranges:
#         for i in range(100):
#             list2 = [random.randint(1, 100) for i in range(t)]
#             start = time.time()
#             quicksort(list2, 0, len(list2)-1)
#             end = time.time()
#             results.append(end-start)
#     pylab.figure(1)
#     p1, = pylab.plot([i for i in range(100)], results[0:100])
#     p2, = pylab.plot([i for i in range(100)], results[100:200])
#     p3, = pylab.plot([i for i in range(100)], results[200:])
#     pylab.show()