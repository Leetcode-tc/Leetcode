# 给定循环升序列表中的一个点，写一个函数向这个列表中插入一个新元素，使这个列表仍然是循环升序的。给定的可以是这个列表中任意一个顶点的指针，并不一定是这个列表中最小元素的指针。

# 如果有多个满足条件的插入位置，你可以选择任意一个位置插入新的值，插入后整个列表仍然保持有序。

# 如果列表为空（给定的节点是 null），你需要创建一个循环有序列表并返回这个点。否则。请返回原先给定的节点。

# 找到链表最小节点 -> 找到插入位置 -> 插入

class Solution:
    def insert(self, head, insertVal):
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
        
        cur = head
        next = head.next
        while cur.val <= next.val:
            cur = cur.next
            next = next.next
            if cur == head:
                break
        min_head = next
        
        while next.val < insertVal:
            cur = next
            next = next.next
            
            if next == min_head:
                break
        cur.next = Node(insertVal)
        cur.next.next = next
        
        return head

# 如果链表为空
# 如果链表不为空
# 如果转一圈没有找到该插入的位置，则将node插入头节点的前面



    
