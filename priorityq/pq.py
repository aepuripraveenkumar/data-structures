
class PriorityObj(object):

    def __init__(self, priority, msg):
        self.priority = priority
        self.message = msg

class PriorityQ(object):


    def __init__(self):
        self.priority_q = []
        self.pq_index = 0

    def _swap_up(self):
        push_index = self.pq_index - 1
        parent_index = (push_index-1)//2
        while parent_index > -1:
            if self.priority_q[parent_index].priority < \
                    self.priority_q[push_index].priority:
                self.priority_q[parent_index], self.priority_q[push_index] \
                    = self.priority_q[push_index], \
                    self.priority_q[parent_index]
                parent_index, push_index = (parent_index-1)//2, parent_index
            else:
                parent_index = -1  #changed to break out of loop


    def _swap_down(self):
        swap_index = 0
        while True:
            child = (2 * swap_index) + 1
            if child > len(self.priority_q) - 1 or child+1 > len(self.priority_q) - 1:
                break
            if self.priority_q[child] <= self.priority_q[child+1]:
                child += 1

            if self.priority_q[swap_index].priority < \
                    self.priority_q[child].priority:
                self.priority_q[swap_index], self.priority_q[child] = \
                    self.priority_q[child], self.priority_q[swap_index]
                swap_index = child
            if self.priority_q[child].priority < \
                    self.priority_q[child+1].priority:
                self.priority_q[child].priority, \
                    self.priority_q[child+1].priority = \
                    self.priority_q[child+1].priority, \
                    self.priority_q[child].priority
            else:
                break


    def insert(self, priority, msg):
        self.priority_q.append(PriorityObj(priority, msg))
        self.pq_index = len(self.priority_q)
        self._swap_up()

    def pop(self):
        try:
            self.priority_q[0] = self.priority_q.pop()
        except IndexError:
            raise
        else:
            self._swap_down()

    def peek(self):
        try:
            return self.priorty_q[0].priority + '-- ' + \
                self.priorty_q[0].message
        except IndexError:
            print "The priority queue is empty."
