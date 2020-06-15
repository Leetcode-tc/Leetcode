class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stackPush = []
        self.stackPop = []


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stackPush.append(x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if len(self.stackPop) != 0:
            return self.stackPop.pop()
        else:
            while len(self.stackPush) != 0:
                self.stackPop.append(self.stackPush.pop())
            return self.stackPop.pop()


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if len(self.stackPop) != 0:
            return self.stackPop[-1]
        else:
            while len(self.stackPush) != 0:
                self.stackPop.append(self.stackPush.pop())
            return self.stackPop[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.stackPush) == 0 and len(self.stackPop) == 0

# 1. 如果stackPush要往stackPop中倒入数据，那么必须要把stackPush中的所有数据一次性倒完；
# 2. 如果stackPop中有数据，则不能发生倒数据的行为；

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
