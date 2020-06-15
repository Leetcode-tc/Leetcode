class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        deque = collections.deque()
        res = []
        for i, num in enumerate(nums):
            while deque and deque[0] <= i-k:
                deque.popleft()
            while deque and num > nums[deque[-1]]:
                deque.pop()
            deque.append(i)
            if i >= k-1:                    # 刚开始遍历时，L和R都为0，有一个形成窗口的过程，此过程没有最大值，L不动，R向右移。
                res.append(nums[deque[0]])
        return res
    

#  滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7


# 双端队列qmax={}, 双端队列存放着数组中的下标值, 数组中的数要从大到小排序
# 假设当前数为arr[i], 放入规则如下：
#       1. 如果qmax为空, 直接把下标i放入qmax中;
#       2. 如果qmax不为空, 取出当前qmax队尾存放的下标j,
#             如果arr[j] > arr[i], 直接把下标i放入qmax的队尾;
#             如果arr[j] <= arr[i], 则一直从qmax的队尾弹出下标, 直到某个下标在qmax中对应的值大于arr[i],
#             把i放入qmax队尾；
# 假设当前数为arr[i], 弹出规则如下：
#       如果qmax 队头的下标等于i-k, 弹出qmax当前队头的下标；
