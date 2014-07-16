import random
import time


def sort(sort_l):
    start_time = time.time()
    for i, _ in enumerate(sort_l):
        j = i
        while j and sort_l[j - 1] > sort_l[j]:
            sort_l[j - 1], sort_l[j] = sort_l[j], sort_l[j - 1]
            j -= 1
    end_time = time.time()
    return end_time - start_time


if __name__ == "__main__":

    item_size = [1000, 10000]
    for i in item_size:
        unsorted = [random.randint(0, i) for j in range(i)]
        total_time = sort(unsorted)
        print "Random sort for %i items took %f" % (i, total_time)
        unsorted.sort()
        total_time = sort(unsorted)
        print "Best case sort for %i items took %f" % (i, total_time)
        unsorted.sort(reverse=True)
        total_time = sort(unsorted)
        print "Worst case sort for %i items took %f" % (i, total_time)
