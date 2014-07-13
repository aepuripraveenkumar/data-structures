
class HashTable(object):

    def __init__(self, size):
        self.size = size
        self.hash_t = dict((i, {}) for i in range(self.size))

    def hash(self, key):
        index = 0
        for ch in key:
            index += ord(ch)
        return index % self.size

    def set(self, key, value):
        self.hash_t[self.hash(key)][key] = value

    def get(self, key):
        index = self.hash(key)
        if key in self.hash_t[index].keys():
            return self.hash_t[index][key]
        raise KeyError
