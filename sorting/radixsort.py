from math import log
import random
import time


def radix_sort(unsorted, base=10):
    if isinstance(unsorted[0], str):
        unsorted = radix_str_sort(unsorted)
    else:
        max_values = int(round(log(max(i for i in unsorted), base)) + 1)
        for place in range(max_values):
            unsorted = sort(unsorted, place, base)
    return unsorted


def sort(unsorted, place, base):
    place_lists = [[] for _ in xrange(base)]
    new_list = []
    for i in unsorted:
        place_lists[(i // base ** place) % base].append(i)
    for i in range(len(place_lists)):
        for j in range(len(place_lists[i])):
            new_list.append(place_lists[i][j])
    return new_list


def radix_str_sort(unsorted):
    num_strings = len(unsorted)
    max_values = max(len(i) for i in unsorted)
    for i in range(len(unsorted)):
        unsorted[i] = list(unsorted[i])
        for j in range(len(unsorted[i])):
            unsorted[i][j] = ord(unsorted[i][j])
    for place in range(1, max_values + 1):
        unsorted = sort_strs(unsorted, place, num_strings)
    for i in range(len(unsorted)):
        for j in range(len(unsorted[i])):
            unsorted[i][j] = chr(unsorted[i][j])
        unsorted[i] = ''.join(unsorted[i])
    return unsorted


def sort_strs(unsorted, place, num_strings):
    place_lists = [[] for _ in xrange(256)]
    new_list = []
    for i in range(num_strings):
        if place > len(unsorted[i]) - 1:
            place_lists[unsorted[i][0]].append(unsorted[i])
        else:
            place_lists[unsorted[i][place]].append(unsorted[i])

    for i in range(len(place_lists)):
        new_list.extend(place_lists[i])
    return new_list


if __name__ == "__main__":
    my_list = ['z', 'car', 'horse', 'whale', 'antelope', 'dog', 'cat']
    sorted = radix_sort(my_list)
    print sorted
    item_size = [1000, 10000, 100000, 1000000]
    for i in item_size:
        unsorted = [random.randint(0, i) for j in range(i)]
        start_time = time.time()
        radix_sort(unsorted)
        end_time = time.time()
        total = end_time - start_time
        print "Random sort for %i items took %f" % (i, total)
        start_time = time.time()
        radix_sort(unsorted)
        end_time = time.time()
        total = end_time - start_time
        print "Best case sort for %i items took %f" % (i, total)
        unsorted.sort(reverse=True)
        start_time = time.time()
        radix_sort(unsorted)
        end_time = time.time()
        total = end_time - start_time
        print "Worst case sort for %i items took %f" % (i, total)
