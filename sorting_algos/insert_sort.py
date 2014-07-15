

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

if __name__ == '__main__':
    