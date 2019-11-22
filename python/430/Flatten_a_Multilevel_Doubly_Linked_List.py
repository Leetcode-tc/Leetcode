"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        stack = []
        p = head
        while p:
            if p.child:
                if p.next:
                    next = p.next
                    next.prev = None
                    stack.append(next)
                p.next = p.child
                p.child = None
                p.next.prev = p
            pre = p
            p = p.next
            if not p and len(stack)>0:
                node = stack.pop()
                pre.next = node
                node.prev = pre
                p = node
        return head

# 遍历
# 没有child就跳next
# 有child就把next压栈，修改自身next和child的prev，然后跳child
# 重复2，3，直到没有next执行5
# 出栈获取当前层上一层的中断点，将其与当前层的尾节点连上
# 重复2，3，4，5直到next为null，栈为空
