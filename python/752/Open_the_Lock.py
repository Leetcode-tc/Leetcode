class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        if target == '0000':
            return 0
        # 初始化根节点
        q = []
        q.append(('0000', 0))
        # 开始循环队列
        while q:
            # 取出一个节点
            node, step = q.pop(0)
            # 放入周围节点
            for i in range(4):
                for add in (1,-1):
                    cur = node[:i] + str((int(node[i]) + add) % 10) + node[i+1:]
                    if cur == target:
                        return step + 1
                    if not cur in deadends:
                        q.append((cur, step +1))
                        deadends.add(cur)   # 避免重复搜索
        return -1
