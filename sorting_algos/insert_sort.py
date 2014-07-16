import random
import time
# import pylab


def insertionSort(uList):
    """
    implementation of insertion sort
    worst case: n2
    """

    for i in range(1, len(uList)):
        current = uList[i]
        index = i
        while uList[index-1] > current and index > 0:
            uList[index], uList[index-1] = uList[index-1], current
            index -= 1

# if __name__ == '__main__':
#     results = []
#     ranges = [10, 100, 1000]
#     for t in ranges:
#         for i in range(100):
#             list2 = [random.randint(1, 100) for i in range(t)]
#             start = time.time()
#             insertionSort(list2)
#             end = time.time()
#             results.append(end-start)
#     pylab.figure(1)
#     p1, = pylab.plot([i for i in range(100)], results[0:100])
#     p2, = pylab.plot([i for i in range(100)], results[100:200])
#     p3, = pylab.plot([i for i in range(100)], results[200:])
#     pylab.show()
