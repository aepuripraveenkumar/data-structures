
class BinHeap(object):


    def __init__(self, items = None):
        self.heap_list = []
        self.list_index = 0
        if items:
            for i in items:
                self.push(i)

    def _swap(self):
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

    def push(self, value):
        self.heap_list.append(value)
        self.list_index = len(self.heap_list)
        self._swap()

    def pop(self):
        pass