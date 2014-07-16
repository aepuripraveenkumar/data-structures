import random
import time


def merge_sort(list_u):
    # If list is less than 2 elements in size
    if len(list_u) < 2:
        return list_u

    middle = len(list_u) / 2
    list_ul = list_u[:middle]
    list_ur = list_u[middle:]
    list_ul = merge_sort(list_ul)
    list_ur = merge_sort(list_ur)
    return merge(list_ul, list_ur)


def merge(left, right):
    list_s = []
    while left or right:
        if left and right:
            if left[0] <= right[0]:
                list_s.append(left[0])
                left.pop(0)
            else:
                list_s.append(right[0])
                right.pop(0)
        elif left:
            list_s.append(left[0])
            left.pop(0)
        else:
            list_s.append(right[0])
            right.pop(0)
    return list_s

if __name__ == "__main__":
    item_size = [1000, 10000]
    for i in item_size:
        unsorted = [random.randint(0, i) for j in range(i)]
        start_time = time.time()
        result = merge_sort(unsorted)
        end_time = time.time()
        total = end_time - start_time
        print "Random sort for %i items took %f" % (i, total)
        start_time = time.time()
        result = merge_sort(unsorted)
        end_time = time.time()
        total = end_time - start_time
        print "Best case sort for %i items took %f" % (i, total)
        unsorted.sort(reverse=True)
        start_time = time.time()
        result = merge_sort(unsorted)
        end_time = time.time()
        total = end_time - start_time
        print "Worst case sort for %i items took %f" % (i, total)
