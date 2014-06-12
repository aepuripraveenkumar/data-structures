
class BinHeap(object):


    def __init__(self, items = None):
        self.heap_list = []
        self.list_index = 0
        if items:
            for i in items:
                self.push(i)

    def _swap_up(self):
        push_index = self.list_index - 1
        parent_index = (push_index-1)//2
        while parent_index > -1:
            if self.heap_list[parent_index] < self.heap_list[push_index]:
                self.heap_list[parent_index], self.heap_list[push_index] \
                    = self.heap_list[push_index], \
                    self.heap_list[parent_index]
                swap_index = parent_index
                parent_index = (swap_index-1)//2
                push_index = swap_index
            else:
                parent_index = -1  #changed to break out of loop


    def _swap_down(self):
        swap_index = 0
        while True:
            child = (2 * swap_index) + 1
            if child > len(self.heap_list) - 1 or child+1 > len(self.heap_list) - 1:
                break
            print child, len(self.heap_list) - 1
            if self.heap_list[child] > self.heap_list[child+1]:
                child_index = child
            elif self.heap_list[child] <= self.heap_list[child+1]:
                child_index = child + 1

            if self.heap_list[swap_index] < self.heap_list[child_index]:
                self.heap_list[swap_index], self.heap_list[child_index] = \
                    self.heap_list[child_index], self.heap_list[swap_index]
                swap_index = child_index
            else:
                break


    def push(self, value):
        self.heap_list.append(value)
        self.list_index = len(self.heap_list)
        self._swap_up()

    def pop(self):
        try:
            self.heap_list[0] = self.heap_list.pop()
        except IndexError:
            raise
        else:
            self._swap_down()
