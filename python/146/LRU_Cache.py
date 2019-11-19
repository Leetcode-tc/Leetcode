class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.od = collections.OrderedDict()
        self.cap = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.od:
            return -1
        # self.od.move_to_end(key)
        self.od[key] = self.od.pop(key)
        return self.od[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.od:
            self.od.pop(key)
        elif len(self.od) == self.cap:
            self.od.popitem(last=False)
        self.od[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
