# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        max_val = max(nums)
        max_index = nums.index(max_val)
        root = TreeNode(max_val)
        root.left = self.constructMaximumBinaryTree(nums[:max_index])
        root.right = self.constructMaximumBinaryTree(nums[max_index+1:])
        return root

        # 递归
        # 先找到最大值以及最大值的位置max_index
        # 对于nums[:max_index]递归调用函数，返回值为root.left；对于nums[max_index+1:]递归调用函数，返回值为root.right

        
   
    def constructMaximumBinaryTree_2(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        # 递减栈
        stack = []
        for n in nums:
            cur = TreeNode(n)
            # 当遍历到的元素值cur > 栈顶元素，将栈中所有小于cur节点弹出，此时全部弹出的值一定在cur的左子树;
            # 将最后一个弹出的值记录为node，令cur.left=node即可构造树（此时的node一定是左子树的根）
            while stack and stack[-1].val < n:
                cur.left = stack.pop()
            # 如果当前遍历到的元素cur小于栈顶元素的话，首先将栈顶元素stack[-1].right=cur，然后将其加入栈中
            # （注意对于当前遍历到的元素来说，此时的cur一定是右子树的根）
            if stack:
                stack[-1].right = cur
            stack.append(cur)
        return stack[0]
            
