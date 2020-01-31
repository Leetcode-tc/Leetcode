class Solution(object):
    def dailyTemperaturesStack(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        ret = [0 for _ in range(len(T))]
        for i, x in enumerate(T):
            # 入栈条件：当前元素比栈顶元素小，出栈条件：遇到比自己大的温度
            while stack and T[stack[-1]] < x:
                index = stack.pop()
                ret[index] = i - index  # 出栈时索引距离即天数差
            stack.append(i)
        return ret

    def dailyTemperatures(self, T):
        index = [0 for _ in range(101)]
        ret = [0 for _ in range(len(T))]
        for i in range(len(T)-1, -1, -1):
            for j in range(T[i]+1,101):
                if index[j] != 0 and (ret[i] == 0 or ret[i] > index[j]-i):
                    ret[i] = index[j] - i
            index[T[i]] = i
        return ret
