class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        if len(arr) == 1:
            return min(target, arr[0])
        left, right = target/len(arr), max(arr)
        while left < right-1:
            mid = left + (right-left)/2
            tmp = sum(map(lambda x:x if x<mid else mid, arr))
            if tmp >= target:
                right = mid
            else:
                left = mid
        left_sum = sum(map(lambda x: x if x<left else left, arr))
        right_sum = sum(map(lambda x: x if x<right else right, arr))
        return left if abs(left_sum-target) <= abs(right_sum-target) else right
